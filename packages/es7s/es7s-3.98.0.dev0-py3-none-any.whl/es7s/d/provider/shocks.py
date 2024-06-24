# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import re
import socket
import struct
from datetime import datetime
from subprocess import CompletedProcess

import pytermor as pt
import requests

from es7s.shared import ShocksInfo, ShocksProxyInfo
from es7s.shared import get_merged_uconfig, get_logger, run_subprocess, SocketTopic
from ._base import DataProvider


class ShocksProvider(DataProvider[ShocksInfo]):
    def __init__(self):
        super().__init__("shocks", SocketTopic.SHOCKS, 11.0)
        self._config = get_merged_uconfig()
        self._config_section = "provider." + self._config_var
        self._proxy_configs = self._config.get_subsections(self._config_section)
        self._check_url = self._config.get_section(self._config_section).get("check-url")

        self._connect_check_cache: list[tuple[bool, float] | None] = [None] * len(
            self._proxy_configs
        )
        self._connect_check_num = 0  # for round-robining

    def _reset(self):
        self._connect_check_cache = [None] * len(self._connect_check_cache)
        return ShocksInfo()

    def _collect(self) -> ShocksInfo:
        p: CompletedProcess = run_subprocess("pgrep", "-f", "/ssh\\s.*-[LDR]", check=False)
        tunnels_amount = len(p.stdout.splitlines())
        running_amount = 0
        healthy_amount = 0

        try:
            self._network_req_event.set()
            p: CompletedProcess = run_subprocess("netstat", "-tula")
        finally:
            self._network_req_event.clear()
        relay_listeners_amount = len({*re.findall(R"(1002\d).+LISTEN", p.stdout)})
        relay_connections_amount = len(
            {*re.findall(R"(1002\d).+ESTABLISH", p.stdout)}
        )  # @TODO read shocks relay port from config?

        p = run_subprocess("systemctl", "list-units", "--no-pager", "--no-legend", "es7s-shocks@*")
        workers_up = [re.search(r"@(.+?)\.service", s).group(1) for s in p.stdout.splitlines()]

        proxy_infos = []
        for idx, subsection in enumerate(self._proxy_configs):
            name = subsection.split(".")[-1]
            proxy_info = self._probe_proxy(idx, name, subsection, name in workers_up)
            proxy_infos.append(proxy_info)
            if proxy_info.running:
                running_amount += 1
            if proxy_info.healthy:
                healthy_amount += 1
            get_logger().debug(f"Collected data {proxy_info!r}")

        self._connect_check_num += 1
        return ShocksInfo(
            tunnels_amount,
            running_amount,
            healthy_amount,
            frozenset(proxy_infos),
            relay_listeners_amount,
            relay_connections_amount,
        )

    def _probe_proxy(
        self, idx: int, name: str, subsection: str, worker_up: bool
    ) -> ShocksProxyInfo:
        result = ShocksProxyInfo(name, worker_up=worker_up)
        if not worker_up:
            return result

        ucs = self._config.get_section(subsection)
        proxy_host = ucs.get("proxy-host")
        proxy_port = ucs.get("proxy-port", rtype=int)
        proxy_url = f"{ucs.get('proxy-protocol')}://{proxy_host}:{proxy_port}"

        check_url = self._check_url
        if override_check_url := ucs.get("check-url", fallback=None):
            check_url = override_check_url

        result.proxy_latency_s = self._check_proxy_is_up(proxy_host, proxy_port)
        if result.proxy_latency_s is False:
            return result
        else:
            result.running = True

        if ucs.get("proxy-listening", rtype=bool, fallback=False):
            return result

        logger = get_logger()
        if self._connect_check_num % len(self._proxy_configs) != idx:
            logger.debug(f"Reading cached value for {name}")
            if connect_cache := self._connect_check_cache[idx]:
                result.healthy, result.latency_s = connect_cache
            return result

        try:
            response = self._check_can_connect(idx, proxy_url, check_url)
        except Exception as e:
            logger.error(f"Connectivity error: {e}")
        else:
            if response and response.ok:
                result.healthy = True
                result.latency_s = response.elapsed.total_seconds()
            else:
                logger.error(f"Connectivity error: {response!r}")

        self._connect_check_cache[idx] = (result.healthy, result.latency_s)
        return result

    def _check_proxy_is_up(self, socks_host: str, socks_port: int) -> bool | float:
        sen = struct.pack("BBB", 0x05, 0x01, 0x00)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg_tpl = f"Socks proxy {socks_host}:{socks_port} is %s"
        before_ts = datetime.now().timestamp()
        try:
            s.settimeout(self._get_request_timeout())
            s.connect((socks_host, socks_port))
            s.sendall(sen)
            s.recv(2)
            # data = s.recv(2)
            # version, auth = struct.unpack('BB', data)
            s.close()
        except IOError | OSError as e:
            get_logger().debug(msg_tpl % f"down: {e}")
            return False
        finally:
            after_ts = datetime.now().timestamp()
            proxy_latency = after_ts - before_ts
            s.close()
        get_logger().debug((msg_tpl % "up") + f", proxy latency: {pt.format_time(proxy_latency)}")
        return proxy_latency

    def _check_can_connect(
        self, idx: int, socks_url: str, check_url: str
    ) -> requests.Response | None:
        return self._make_request(
            check_url,
            request_fn=lambda url: requests.get(
                url,
                timeout=self._get_request_timeout(),
                proxies={"http": socks_url, "https": socks_url},
            ),
            log_response_body=False,
        )

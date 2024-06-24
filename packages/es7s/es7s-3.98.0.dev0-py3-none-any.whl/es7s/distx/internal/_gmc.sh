#!/bin/bash
#-------------------------------------------------------------------------------
# es7s/core | &git &m&cdiff wrapper for manual file select
# (c) 2023 A. Shavykin <0.delameter@gmail.com>
#-------------------------------------------------------------------------------

__get_msg() {
  local fmtlabel='\x1b[7m'
  local fmtprompt='\x1b[27m'
  printf "${fmtlabel}[%3d/%3d]${fmtprompt} %b" ${GIT_DIFF_PATH_COUNTER:-0} ${GIT_DIFF_PATH_TOTAL:-0} "$*"
}
__fail() { printf "\r" && __get_msg "$*" && echo && exit 0 ; }
__die() { echo Aborted && exit 1 ; }

declare old=${2:-}
declare new=${5:-}
[[ ! -f "$old" && ! -f "$new" ]] && __fail $'\x1b[2mNot found\x1b[22m \x1b[2m'${old@Q}$' '${new@Q}$'\x1b[22m'

target="\x1b[1m${1@Q}\x1b[22m"

if ! grep -Iq . "$1" &>/dev/null ; then
    __fail "Skipped binary file $target"
fi

read -n 1 -sr -p "$(__get_msg "     Open $target"?) (y/N/q): " yn
echo
[[ $yn =~ [Qq] ]] && __die Aborted
[[ $yn =~ [Yy] ]] || __fail "  Skipped $target"$'\x1b[K'

[[ ! -f "$old" &&   -f "$new" ]] && bat "$new" >/dev/stderr && exit 0
[[   -f "$old" && ! -f "$new" ]] && bat "$old" && exit 0

mcdiff "$@"

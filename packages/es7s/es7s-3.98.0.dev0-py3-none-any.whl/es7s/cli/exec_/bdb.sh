#!/bin/bash
#-------------------------------------------------------------------------------
# es7s/core | &bash &de&bugger
# (c) 2023 A. Shavykin <0.delameter@gmail.com>
# (c) 2022 K. Timofeev <kt97679@gmail.com>
#-------------------------------------------------------------------------------
# shellcheck disable=SC2162,SC1090

_e() { [[ -n $BDB_COLOR_OUTPUT ]] && echo $'\e['"${1:-}"m; }

__dbg__usage() {
    echo "bdb <command> [<command_args>...]"
    echo
    echo "Interactive bash script debugger."
    echo "Runs the <command> with <command_args> and can trace execution steps and/or pause at set breakpoints."
    echo
    echo "Commands:"
    __dbg__commands
    echo
    echo "Environment:"
    echo "  BDB_COLOR_OUTPUT        non-empty string enables colored output"
    echo "  BDB_RCFILE_PATH         path to a file with newline-separated bdb startup commands, e.g.:"
    echo "                              t "
    echo "                              bae 1 "
    echo
    echo "Hint: Use ^D instead of Enter to continue the execution."
}
__dbg__commands() {
    echo "  bdb> h[elp]         display command list"
    echo "  bdb> t[race]        toggle tracing mode [default: off]"
    echo "  bdb> bl             display breakpoint list"
    echo "  bdb> ba <expr>      add new breakpoint: pause if <expr> is true, checked every line of code"
    echo "  bdb> bal <n>        add new breakpoint: pause at line number <n>"
    echo "  bdb> bae <n>        add new breakpoint: pause at every <n> lines"
    echo "  bdb> bd <n>         remove the breakpoint number <n> (as in 'bl' command)"
    echo "  bdb> <command>      run the arbitrary shell command; useful for checking variable values etc."
}

__dbg__breakpoints=()
__dbg__trace=2
__dbg__trap_count=0
__dbg__startup="$([[ -n "$BDB_RCFILE_PATH" ]] && cat < "$BDB_RCFILE_PATH")"
__dbg__trap() {
    local __dbg__cmd __dbg__cmd_args __dbg__set="$(set +o)" \
        __dbg__do_break=false __dbg__breakpoint_num __dbg__breakpoint_idx
    set +eu
    ((__dbg__trap_count++))

    for __dbg__breakpoint_num in $(seq ${#__dbg__breakpoints[@]}); do
        __dbg__breakpoint_idx=$((__dbg__breakpoint_num - 1))
        eval "${__dbg__breakpoints[__dbg__breakpoint_idx]}" && __dbg__do_break=true && break
    done

    ((__dbg__trace == 2)) || $__dbg__do_break && {
        ((__dbg__trace != 2)) \
            && echo -n "$(_e 31)[$__dbg__breakpoint_num] $(_e 36)$(basename "${BASH_SOURCE[1]}"):" \
            && echo "$(_e 32)${BASH_LINENO[0]}: $(_e) $(__dbg_print_command)"

        ((__dbg__trace == 2)) && __dbg__trace=0

        while __dbg_prompt_input ; do
            case $__dbg__cmd in
                   '') eval "$__dbg__set" && return 0 ;;
               h|help) __dbg__commands ;;
              t|trace) ((__dbg__trace ^= 1)) ;;
                   bl) printf "%s\n" "${__dbg__breakpoints[@]}" | grep . | cat -n ;;
                   ba) __dbg__breakpoints+=("$__dbg__cmd_args") ;;
                  bal) __dbg__breakpoints+=("(( BASH_LINENO == $__dbg__cmd_args ))") ;;
                  bae) __dbg__breakpoints+=("(( __dbg__trap_count % $__dbg__cmd_args == 0 ))") ;;
                   bd) unset __dbg__breakpoints[$((__dbg__cmd_args - 1))] \
                         && __dbg__breakpoints=("${__dbg__breakpoints[@]}") ;;
                    *) eval "$__dbg__cmd $__dbg__cmd_args" ;;
            esac
        done
        return
    }

    ((__dbg__trace == 1)) \
        && echo "$(_e 36)${BASH_SOURCE[1]}:$(_e 32)${BASH_LINENO[0]}:$(_e) $(__dbg_print_command)"
}

__dbg_prompt_input() {
  echo "{$__dbg__startup@A}"
  [[ -n "$__dbg__startup" ]] && cat <<< "$__dbg__startup" && __dbg__startup=
  read -p "$(_e 34)bdb> $(_e)" __dbg__cmd __dbg__cmd_args
}
__dbg_print_command() {
    ! command -v bat &> /dev/null && echo "$BASH_COMMAND" && exit
    bat <<< "$BASH_COMMAND" -l bash --no-pager --decorations=never --theme=1337 --color=always
}

[[ $1 =~ ^--?h(elp)? || $# -eq 0 ]] && __dbg__usage && exit
set -T
trap "__dbg__trap >/dev/tty" debug
. "$@"

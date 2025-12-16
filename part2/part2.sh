#!/bin/bash

[[ -n "$1" ]] || { echo "Error: $0 <target_program>"; exit 1; }
prog="$(basename "$1")_part2"

# compile trampoline.
e9compile part2.c

# instrument target program: push on calls, verify on returns.
e9tool \
  -M 'mnemonic=="call"' -P 'shadow_push((static) next)@part2' \
  -M 'mnemonic=="ret"' -P 'shadow_check(*((uint64_t*)(static) mem[0]))@part2' \
  "$1" -o "$prog"

echo ""
./"$prog"

echo ""
cat output.txt

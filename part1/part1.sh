#!/bin/bash

# need one argument.
[[ -n "$1" ]] || { echo "Error: $0 <target_program>"; exit 1; }
prog="$(basename "$1")_part1"

# compile trampoline.
e9compile part1.c

# instrument target program.
e9tool \
    -M 'section(text) && !within(part1)' -P 'instrcounter()@part1' \
    -M 'defined(mem[0]) && section(text) && !within(part1)' -P 'memcounter((static) addr)@part1' \
    "$1" -o "$prog"

# execute instrumented program.
echo ""
./"$prog"

# output the result.
echo ""
cat output.txt

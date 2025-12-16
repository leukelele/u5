# Part 1: Instruction counting

This directory contains the trampoline `part1.c` and driver script `part1.sh`
for counting both all executed instructions and memory-access instructions
    using e9patch.

## Usage

```
./part1.sh <path-to-target-binary>
```

The script compiles the trampoline, rewrites the target binary to inject the
counters (skipping the trampoline itself), runs the patched program, and prints
the counts saved in `output.txt`.

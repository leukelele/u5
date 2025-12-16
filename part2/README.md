# Part 2: Shadow stack example

This code instruments `call` and `ret` instructions with e9patch to maintain a
simple shadow stack.

## Files
- `part2.c`: trampoline with push/verify callbacks and basic reporting to
  `output.txt`.
- `part2.sh`: driver to compile the trampoline and instrument a target binary.

## Usage
```bash
cd part2
./part2.sh /bin/ls
```
The script emits `output.txt` showing final shadow stack depth and terminates
early on mismatches.

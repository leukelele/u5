# Part 3: Postmortem binary patching

This directory contains a minimal, static patcher for the three provided
challenge binaries. Each program overflowed a fixed-size stack buffer by
calling `fgets`/`read` with an argument larger than the allocated
buffer.

## What the patch does
- `bof-level03`: replaces the `fgets` length (`0x40`) with `0x14` to fit
  the 20-byte buffer.
- `21-stack-ovfl-sc-64`: clamps the `read` length from `0x100` down to
  `0x1e` so it matches the 30-byte buffer.
- `rop-1-64`: reduces the `read` length from `0x100` to `0x80` for the
  128-byte buffer.

## Usage
Run the patcher from inside this directory:

```bash
./patch_binaries.py
```

The script writes patched copies next to itself (e.g.,
`bof-level03_patched`). The originals in `../testcases/` remain untouched.

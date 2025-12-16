# Part 3: C trampoline patching workflow

This part replaces the earlier Python helper with a small C trampoline compiled
with `e9compile` and injected with `e9tool`. The trampoline wraps vulnerable
`read`/`fgets` call sites and clamps oversized length arguments so that each
binary receives only the amount of data its stack buffers can safely hold.

## Build and patch

```bash
cd part3
./patch.sh
```

The script compiles `patch.c` into `patch.e9` and rewrites every binary in
`../testcases/`, producing sibling outputs named `<binary>_patched`. Originals
are left untouched so you can diff and test both versions side by side. For
traceability, `patch.sh` also emits `*_patched.objdump` and `*_patched.hexdump`
files capturing the rewritten call sites.

## Length policy

The trampoline resolves a per-binary cap at runtime, matching the known buffer
sizes from the challenges:

- `21-stack-ovfl-sc-64` → 64 byte payload window.
- `bof-level03` → 64 bytes for the stack buffer used by the vulnerable read.
- `heartbleed` → 256 bytes to keep the heartbeat payload within the allocated
  response buffer.
- `rop-1-64` → 128 bytes so the saved return address and ROP chain cannot be
  overrun.

If a binary name does not match any of the above prefixes, the trampoline falls
back to a conservative 64‑byte ceiling.

## Verifying the patch

After running `patch.sh`, inspect the rewritten call sites to confirm the new
length constants are in place:

```bash
objdump -d 21-stack-ovfl-sc-64_patched | grep -n "fgets"
hexdump -C 21-stack-ovfl-sc-64_patched | head -n 5
```

You should see the injected trampolines force lengths that match the caps above
(e.g., a `mov $0x40,%edx` for 64-byte clamps or `0x80`/`0x100` for the larger
limits) instead of the original unbounded reads. Use the generated `.objdump`
files to validate additional call sites without having to re-run objdump.

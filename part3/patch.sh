#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
PATCH_E9="$SCRIPT_DIR/patch.e9"
TARGET_DIR="$SCRIPT_DIR/../testcases"

if ! command -v e9compile >/dev/null 2>&1; then
  echo "e9compile not found in PATH" >&2
  exit 1
fi

if ! command -v e9tool >/dev/null 2>&1; then
  echo "e9tool not found in PATH" >&2
  exit 1
fi

echo "[+] compiling trampoline to $PATCH_E9"
e9compile "$SCRIPT_DIR/patch.c" -o "$PATCH_E9"

echo "[+] patching targets from $TARGET_DIR"
for target in "$TARGET_DIR"/*; do
  [ -f "$target" ] || continue
  base=$(basename -- "$target")
  output="$SCRIPT_DIR/${base}_patched"
  echo "  - $base -> $(basename -- "$output")"
  e9tool --patch "$PATCH_E9" --output "$output" "$target"

  # Capture the patched call sites for documentation/inspection.
  objdump -d "$output" > "$output.objdump"
  head -c 256 "$output" | hexdump -C > "$output.hexdump"
done

echo "[+] done"

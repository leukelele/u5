#!/usr/bin/env python3
"""
Postmortem patches for the three vulnerable challenge binaries.

Each patch replaces the oversized length used by fgets/read with the
corresponding buffer size. The search/replace patterns are kept small
and unique to avoid touching unrelated instructions.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


@dataclass
class Patch:
    name: str
    source: Path
    output: Path
    before: bytes
    after: bytes


PATCHES: Sequence[Patch] = (
    Patch(
        name="bof-level03",
        source=Path("../testcases/bof-level03/bof-level03"),
        output=Path("bof-level03_patched"),
        before=bytes.fromhex("be40000000488d7dd0"),
        after=bytes.fromhex("be14000000488d7dd0"),
    ),
    Patch(
        name="stack-ovfl-sc-64",
        source=Path("../testcases/21-stack-ovfl-sc-64/stack-ovfl-sc-64"),
        output=Path("stack-ovfl-sc-64_patched"),
        before=bytes.fromhex("31ffb90001000089ca488db570ffffff"),
        after=bytes.fromhex("31ffb91e00000089ca488db570ffffff"),
    ),
    Patch(
        name="rop-1-64",
        source=Path("../testcases/rop-1-64/rop-1-64"),
        output=Path("rop-1-64_patched"),
        before=bytes.fromhex("488d4580ba000100004889c6bf00000000"),
        after=bytes.fromhex("488d4580ba800000004889c6bf00000000"),
    ),
)


def apply_patch(patch: Patch) -> None:
    data = patch.source.read_bytes()
    idx = data.find(patch.before)
    if idx == -1:
        raise RuntimeError(f"pattern not found in {patch.source}")

    patched = data[:idx] + patch.after + data[idx + len(patch.before) :]
    patch.output.write_bytes(patched)
    print(f"{patch.name}: patched at offset 0x{idx:x} -> {patch.output}")


def main() -> None:
    for patch in PATCHES:
        apply_patch(patch)


if __name__ == "__main__":
    main()

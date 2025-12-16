The stack is configured as follows:
```x86asm
[rbp+0x8]           return address
[rbp]               saved rbp
[rbp-0x8]           a = 0x4141414141414141
[rbp-0x10]          b = 0x4242424242424242
[rbp-0x18]
[rbp-0x20]
[rbp-0x28]
[rbp-0x30]          buffer
```

Can you overwrite both `a` and `b` to make:
```c
a = 0x6867666564636261
b = 0x4847464544434241
```
and run `get_a_shell()`?

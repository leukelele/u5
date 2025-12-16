# cs6332: Lab5 static binary rewriter (105 points + boust 40 points)

In continuation of Lab 4, which focused on implementing a dynamic binary translator, we now move on to building a static binary rewriter using the [e9patch framework][e9patch], which employs a trampoline-based binary rewriting technique as described in the [e9patch paper].

For this unit, we have prepared three exploitable binaries drawn from past challenges: (1) a buffer-overflow vulnerability, (2) a shellcode exercise, and (3) a ROP challenge. We also provide accompanying pwntools scripts (e.g., ex.py) to launch attacks against these binaries.

All essential resources for this unit are available in the [User Guide] and [Programming Guide]. You may also refer to the [tutorial page][tutorial] for example uses of the e9patch framework in patching and instrumenting binaries. The detailed description of the unit5 can be found from [here](https://codimd.syssec.org/s/EUJInF37H).

---
[tutorial]:https://codimd.syssec.org/s/ZY71YEBHW
[e9patch]:https://github.com/GJDuck/e9patch
[e9patch paper]:https://www.comp.nus.edu.sg/~gregory/papers/e9patch.pdf
[Heartbleed]:https://www.heartbleed.com/
[0d7717f]:https://github.com/openssl/openssl/commit/0d7717fc9c83dafab8153cbd5e2180e6e04cc802
[HeartBleed commit]:https://github.com/openssl/openssl/commit/96db9023b881d7cd9f379b0c154650d6c108e9a3
[HeartBleed patch]:https://cs6332.syssec.org/l/week12/res/heartbleed.patch.txt
[User guide]:https://github.com/GJDuck/e9patch/blob/master/doc/e9tool-user-guide.md
[Programming guide]:https://github.com/GJDuck/e9patch/blob/master/doc/e9patch-programming-guide.md
[unit5.zip]:https://files.syssec.org/unit5.zip# u5

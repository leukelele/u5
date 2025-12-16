# cs6332: Lab5 static binary rewriter (105 points + boust 40 points)

In continuation of Lab 4, which focused on implementing a dynamic binary translator, we now move on to building a static binary rewriter using the [e9patch framework][e9patch], which employs a trampoline-based binary rewriting technique as described in the [e9patch paper].

For this unit, we have prepared three exploitable binaries drawn from past challenges: (1) a buffer-overflow vulnerability, (2) a shellcode exercise, and (3) a ROP challenge. We also provide accompanying pwntools scripts (e.g., ex.py) to launch attacks against these binaries.

All essential resources for this unit are available in the [User Guide] and [Programming Guide]. You may also refer to the [tutorial page][tutorial] for example uses of the e9patch framework in patching and instrumenting binaries. The detailed description of the unit5 can be found from [here](https://codimd.syssec.org/s/EUJInF37H).

## Assignment tasks

### Part 1: Instruction counting (20 pt)

Extend the tutorial template to rewrite the target binary so it counts **all executed instructions** and **all memory-access instructions (reads and writes)**. The patched program should print both totals, similar to the sample output shown below:

```
==================================================
Number of all instruction executed: 123456789
Number of memory instruction executed: 9876543
==================================================
```

Avoid instrumenting the analysis routine on every single instruction (see §5.3 of the e9patch paper) to prevent trampoline conflicts.

### Part 2: Shadow Stack (40 pt)

Instrument `call` and `ret` instructions to maintain a shadow stack, reusing earlier ShadowStacks labs as needed. The rewriter cannot patch external libraries (e.g., `printf` in libc), so ensure the shadow stack tolerates benign inputs while still blocking control-flow hijacking attempts.

An example implementation lives in `part2/`. Run it with:

```
cd part2
./part2.sh /bin/ls
```

### Part 3: Postmortem patching (45 pt)

Patch the provided vulnerable binaries after the fact to align their input lengths with the actual buffer sizes. A minimal patcher that rewrites the offending `fgets`/`read` lengths for all three supplied programs lives in `part3/`.

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

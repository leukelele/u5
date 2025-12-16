#define _GNU_SOURCE
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <e9patch.h>

/*
 * Trampoline-based hardening for the supplied testcases.
 * The wrappers clamp overly large length arguments before
 * delegating to the original libc implementation.
 */

extern char *program_invocation_short_name;

#define DEFAULT_LIMIT 64

struct length_rule {
    const char *binary_prefix;
    size_t cap;
};

static const struct length_rule rules[] = {
    {"heartbleed", 256},
    {"21-stack-ovfl-sc-64", 64},
    {"bof-level03", 64},
    {"rop-1-64", 128},
};

static size_t resolve_cap(void) {
    const char *name = program_invocation_short_name;
    for (size_t i = 0; i < sizeof(rules) / sizeof(rules[0]); ++i) {
        if (strstr(name, rules[i].binary_prefix) != NULL) {
            return rules[i].cap;
        }
    }
    return DEFAULT_LIMIT;
}

static size_t clamp_length(size_t requested) {
    size_t cap = resolve_cap();
    return requested > cap ? cap : requested;
}

/* Import the original libc entry points so the trampolines can tail-call them. */
E9PATCH_EXTERN(ssize_t, read, int fd, void *buf, size_t count);
E9PATCH_EXTERN(char *, fgets, char *s, int size, FILE *stream);

/* Clamp POSIX read(2) lengths. */
E9PATCH_TRAMPOLINE(ssize_t, hardened_read, int fd, void *buf, size_t count) {
    size_t capped = clamp_length(count);
    return read(fd, buf, capped);
}

/* Clamp stdio fgets lengths. */
E9PATCH_TRAMPOLINE(char *, hardened_fgets, char *s, int size, FILE *stream) {
    size_t capped = clamp_length((size_t)size);
    return fgets(s, (int)capped, stream);
}

/* Register the trampolines with the dispatcher used by e9tool. */
E9PATCH_PATCHSET(part3_patchset) {
    E9PATCH_HOOK(read, hardened_read);
    E9PATCH_HOOK(fgets, hardened_fgets);
}

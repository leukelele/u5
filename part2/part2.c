#include "stdlib.c"

#define SHADOW_MAX 65536

static uint64_t shadow_stack[SHADOW_MAX];
static size_t shadow_top = 0;
static FILE *out = NULL;

static void unsafe_abort(const char *msg, uint64_t got, uint64_t expect) {
    out = fopen("output.txt", "w");
    fprintf(out, "Shadow stack violation: %s\n", msg);
    fprintf(out, " expected=0x%016llx got=0x%016llx\n", expect, got);
    fclose(out);
    _exit(1);
}

void shadow_push(const void *retaddr) {
    if (shadow_top >= SHADOW_MAX) {
        unsafe_abort("stack overflow", 0, 0);
    }
    shadow_stack[shadow_top++] = (uint64_t)retaddr;
}

void shadow_check(uint64_t retaddr) {
    if (shadow_top == 0) {
        unsafe_abort("stack underflow", retaddr, 0);
    }

    // Allow benign external calls by discarding frames until the return address matches.
    while (shadow_top > 0 && shadow_stack[shadow_top - 1] != retaddr) {
        shadow_top--;
    }

    if (shadow_top == 0 || shadow_stack[shadow_top - 1] != retaddr) {
        unsafe_abort("mismatched return", retaddr, 0);
    }

    shadow_top--;
}

void init(void) {
    shadow_top = 0;
}

void fini(void) {
    out = fopen("output.txt", "w");
    fprintf(out, "Shadow stack depth at exit: %zu\n", shadow_top);
    fclose(out);
}

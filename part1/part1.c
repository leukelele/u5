#include "stdlib.c"

static FILE *out = NULL;
static uint64_t mem_counter = 0;
static uint64_t instr_counter = 0;

void memcounter(const void *addr) {
    (void)addr;
    mem_counter++;
}

void instrcounter(void) {
    instr_counter++;
}

/*
 * Init.
 */
void init(void)
{
    ; // initializer
}

/*
 * Fini.
 */
void fini(void)
{
    out = fopen("output.txt", "w");
    if (!out) {
        return;
    }

    fprintf(out, "===================================================\n");
    fprintf(out, "Number of all instruction executed: %llu\n", instr_counter);
    fprintf(out, "Number of memory instruction executed: %llu\n", mem_counter);
    fprintf(out, "===================================================\n");
    fclose(out);
}

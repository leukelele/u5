CC=clang

all: bof-level03

bof-level03: bof-level03.c
	$(CC) -o $@ $< -fno-stack-protector -U_FORTIFY_SOURCE -O0

clean:
	rm -rf bof-level03

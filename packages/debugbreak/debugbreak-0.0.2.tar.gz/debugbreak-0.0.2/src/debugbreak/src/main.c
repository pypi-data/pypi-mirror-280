// gcc -shared -o debugbreak.dll -export-all-symbols src/main.c

#include <stdio.h>
#include <stdint.h>

void start_debug() {
    __debugbreak();
}

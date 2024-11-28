// Compiling this program will cause a compiler warning, since the function "print_some_stuff"
// is used before it is declared and defined. The program will still run correctly but it is not up to standard.
#include <stdio.h>

void main() {
  print_some_stuff();
}

void print_some_stuff() {
  printf("Hello from a function!\n");
}
// See the correct approach in the file "correct-func-order.c"

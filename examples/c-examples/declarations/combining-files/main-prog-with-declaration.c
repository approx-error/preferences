// This program can be comiled with the file "other-file.c" without a compiler warning since the function is declared beofre it is used
#include <stdio.h>

void func_from_another_file();

void main() {
  func_from_another_file();
}

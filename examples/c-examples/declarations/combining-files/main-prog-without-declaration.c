// Compiling this with "other-file.c" will cause a compiler warning even if "other-file.c" is
// processed first. To stop the compiler warning when you don't want to use header file,
// see the file "main-prog-with-declaration.c"
#include <stdio.h>

void main() {
  func_from_another_file();
}

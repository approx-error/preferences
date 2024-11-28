// Compiling this program won't cause a compiler warning, since the function "print_some_stuff" is declared (and defined) before it is used
#include <stdio.h>

void print_some_stuff() {
  printf("Hello from a function!\n");
}

void main() {
  print_some_stuff();
}

// Another possibility is to first declare the function before using it and defining it after the main function.
// Another possibility still (and a preferred one for bigger projects) is to declare the function in a header file
// and define it in a completely different file. Then if the header file is included at the top the function will
// be declared and if the file containing the file is provided when compilation is done the function can also be used
// Technically header files aren't needed for multi-file compiling but the compiler will still throw a warning,
// if a function from outside a file isn't declared in the file before using it even if the file containing said
// function is processed firts by the compiler. See the sibling directory "combining-files" for an example

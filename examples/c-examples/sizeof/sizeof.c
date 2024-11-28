// Printing the sizes of various c data types
#include <stdio.h>
#include <limits.h>
#include <float.h>

void main() {
  // Chars
  printf("CHARS\n");
  printf("char: size %lu bytes, min: %d, max: %d\n", sizeof(char), CHAR_MIN, CHAR_MAX);
  printf("signed char: size %lu bytes, min: %d, max: %d\n", sizeof(signed char), SCHAR_MIN, SCHAR_MAX);
  printf("unsigned char: size %lu bytes, min: %d, max: %d\n\n", sizeof(unsigned char), 0, UCHAR_MAX);

  // Ints
  printf("INTS\n");
  printf("short: size %lu bytes, min: %d, max: %d\n", sizeof(short), SHRT_MIN, SHRT_MAX);
  printf("short int: size %lu bytes, min: %d, max: %d\n", sizeof(short int), SHRT_MIN, SHRT_MAX);
  printf("signed short: size %lu bytes, min: %d, max: %d\n", sizeof(signed short), SHRT_MIN, SHRT_MAX);
  printf("signed short int: size %lu bytes, min: %d, max: %d\n\n", sizeof(signed short int), SHRT_MIN, SHRT_MAX);

  printf("unsigned short: size %lu bytes, min: %d, max: %d\n", sizeof(unsigned short), 0, USHRT_MAX);
  printf("unsigned short int: size %lu bytes, min: %d, max: %d\n\n", sizeof(unsigned short int), 0, USHRT_MAX);
  
  printf("int: size %lu bytes, min: %d, max: %d\n", sizeof(int), INT_MIN, INT_MAX);
  printf("signed: size %lu bytes, min: %d, max: %d\n", sizeof(signed), INT_MIN, INT_MAX);
  printf("signed int: size %lu bytes, min: %d, max: %d\n\n", sizeof(signed int), INT_MIN, INT_MAX);

  printf("unsigned: size %lu bytes, min: %d, max: %u\n", sizeof(unsigned), 0, UINT_MAX);
  printf("unsigned int: size %lu bytes, min: %d, max: %u\n\n", sizeof(unsigned int), 0, UINT_MAX);

  printf("long: size %lu bytes, min: %ld, max: %ld\n", sizeof(long), LONG_MIN, LONG_MAX);
  printf("long int: size %lu bytes, min: %ld, max: %ld\n", sizeof(long int), LONG_MIN, LONG_MAX);
  printf("signed long: size %lu bytes, min: %ld, max: %ld\n", sizeof(signed long), LONG_MIN, LONG_MAX);
  printf("signed long int: size %lu bytes, min: %ld, max: %ld\n\n", sizeof(signed long int), LONG_MIN, LONG_MAX);

  printf("unsigned long: size %lu bytes, min: %d, max: %lu\n", sizeof(unsigned long), 0, ULONG_MAX);
  printf("unsigned long int: size %lu bytes, min: %d, max: %lu\n\n", sizeof(unsigned long int), 0, ULONG_MAX);

  printf("long long: size %lu bytes, min: %lld, max: %lld\n", sizeof(long long), LLONG_MIN, LLONG_MAX);
  printf("long long int: size %lu bytes, min: %lld, max: %lld\n", sizeof(long long int), LLONG_MIN, LLONG_MAX);
  printf("signed long long: size %lu bytes, min: %lld, max: %lld\n", sizeof(signed long long), LLONG_MIN, LLONG_MAX);
  printf("signed long long int: size %lu bytes, min: %lld, max: %lld\n\n", sizeof(signed long long int), LLONG_MIN, LLONG_MAX);

  printf("unsigned long long: size %lu bytes, min: %d, max: %llu\n", sizeof(unsigned long long), 0, ULLONG_MAX);
  printf("unsigned long long int: size %lu bytes, min: %d, max: %llu\n\n", sizeof(unsigned long long int), 0, ULLONG_MAX);

  // Floats
  printf("FLOATS\n");
  printf("float: size %lu bytes, min: %e, min absolute: %e  max: %e\n", sizeof(float), -FLT_MAX, FLT_MIN, FLT_MAX);
  printf("double: size %lu bytes, min: %le, min absolute: %le  max: %le\n", sizeof(double), -DBL_MAX, DBL_MIN, DBL_MAX);
  printf("long double: size %lu bytes, min: %Le, min absolute: %Le  max: %Le\n", sizeof(long double), -LDBL_MAX, LDBL_MIN, LDBL_MAX);
  
}

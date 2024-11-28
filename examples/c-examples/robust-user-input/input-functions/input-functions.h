#ifndef INPUT_FUNCTIONS_H
#define INPUT_FUNCTIONS_H
#include "../dyn-array/dyn-char-array.h"
#include "../dyn-array/dyn-int-array.h"

enum return_codes {
  INPUT_OK,
  NO_INPUT,
  TOO_LONG_INPUT,
  SMALL_BUFFER,
  ALLOCATION_FAIL,
  INVALID_SPECIFIER,
  INVALID_CHARACTER
};

int get_user_input(char *prompt_string, char *buffer, size_t buffer_size);
// Temporary:
// int parse_format_string(char *format_string, char_list *storage_list);
int parse_user_input(char *buffer_to_scan, char *format_string, int items_expected,
                     int *occurences, char_list *characters, int_list *integers);

#endif

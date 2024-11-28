#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "../dyn-array/dyn-char-array.h"
#include "../dyn-array/dyn-int-array.h"
#include "input-functions.h"

int get_user_input(char *prompt_string, char *buffer, size_t buffer_size) {

  int ch, extra;

  if (buffer_size < 2) {
    return SMALL_BUFFER;
  }

  if (prompt_string != NULL) {
    printf("%s", prompt_string);
    fflush(stdout);
  }

  if (fgets(buffer, buffer_size, stdin) == NULL) {
    return NO_INPUT;
  }

  size_t len = strlen(buffer);
  if (len < 1)
    return NO_INPUT;

  if (buffer[len - 1] != '\n') {
    extra = 0;
    while (((ch = getchar()) != '\n') && (ch != EOF)) {extra = 1;}
    return (extra == 1) ? TOO_LONG_INPUT : INPUT_OK;
  }

  buffer[len - 1] = '\0';
  return INPUT_OK;
}

static bool find_character(char *string_to_search, char char_to_look_for) {

  bool found = false;
  char *current_character = string_to_search;

  while (*current_character != '\0') {
    if (*current_character == char_to_look_for) {
      found = true;
    }
    current_character++;
  } 
  
  return found;
}

static int parse_format_string(char *format_string, char_list *storage_list) {

  char SUPPORTED_SPECS[] = "cd";
  
  char *current_character = format_string;
  char target;
  bool found;

  while (*current_character != '\0') {
    if (*current_character == '%') {
      target = *(current_character + 1);
      found = find_character(SUPPORTED_SPECS, target);
      if (found) {
        add_new_element(storage_list, target);
      } else {
        return INVALID_SPECIFIER;
      }
    }
    current_character++;
  }
  return 0;
}

static int count_occurences(char *parsed_format_string, int *occurences) {
  /* occurences must be a pointer to a two-element array with all elements zero  */

  int length = strlen(parsed_format_string);

  for (int i = 0; i < length; i++) {
    switch (parsed_format_string[i]) {
      case 'c':
        occurences[0] += 1;
        break;
      case 'd':
        occurences[1] += 1;
        break;
      default:
        return INVALID_SPECIFIER;
    }    
  }
  return 0;
}

static int tokenize_and_store(char *buffer_to_scan, char *parsed_format_string, int items_expected,
                              char_list *characters, int_list *integers) {
  
  char *current_character = parsed_format_string;

  char *token;
  int counter = 0;
  int char_id = 0;
  int int_id = 0;
  char *rest = buffer_to_scan;
  while ((token = strtok_r(rest, " ", &rest))) {
    if (counter == items_expected) {
      break;
    }

    //printf("Current token: %s\n", token);
    switch (*current_character) {
      case 'c':
        characters->contents[char_id++] = *token;
        break;
      case 'd':
        char *endptr;
        long int num = strtol(token, &endptr, 10);
        if (endptr == token || *endptr != '\0') {
          return INVALID_CHARACTER ;
        } else {
          integers->contents[int_id++] = num;
          break;
        }

    }
    current_character++;
    counter++;
  }
  return 0;
}

int parse_user_input(char *buffer_to_scan, char *format_string, int items_expected,
                     int *occurences, char_list *characters, int_list *integers) {
  
  char_list parsed_fmt;
  parsed_fmt.number_of_items = 0;
  parsed_fmt.size = 1;
  parsed_fmt.contents = malloc(parsed_fmt.size * sizeof(char));

  if (parsed_fmt.contents == NULL) {
    printf("Allocation fail\n");
    free(parsed_fmt.contents);
    return ALLOCATION_FAIL;
  }

  int status = parse_format_string(format_string, &parsed_fmt);
  if (status == INVALID_SPECIFIER) {
    printf("Invalid format specifier found\n");
    free(parsed_fmt.contents);
    parsed_fmt.contents = NULL;
    return INVALID_SPECIFIER;
  }

  status = count_occurences(parsed_fmt.contents, occurences);
  if (status == INVALID_SPECIFIER) {
    printf("Somehow an invalid specifier was found in the parsed format string!\n");
    free(parsed_fmt.contents);
    parsed_fmt.contents = NULL;
    return INVALID_SPECIFIER;
  }

  //printf("Occurences: c: %d, d: %d\n", occurences[0], occurences[1]);
  for (int i = 0; i < occurences[0]; i++) {
    add_new_element(characters, '0');
  }

  for (int i = 0; i < occurences[1]; i++) {
    add_new_integer(integers, 0);
  }

  status = tokenize_and_store(buffer_to_scan, parsed_fmt.contents, items_expected, characters, integers);
  if (status == INVALID_CHARACTER) {
    printf("Invalid number!\n");
    return INVALID_CHARACTER;
  }
  // Eventually:
  free(parsed_fmt.contents);
  parsed_fmt.contents = NULL;

  return 0;
}

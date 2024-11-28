#include <stdio.h>
#include <stdlib.h>
#include "input-functions/input-functions.h"
#include "dyn-array/dyn-char-array.h"
#include "dyn-array/dyn-int-array.h"

int main() {

  char buffer[20];
  size_t buffer_size = sizeof(buffer);
  char prompt[] = "Input ints and chars in the following format: c i i i c i c\n20 characters can fit into the buffer\n>>> ";
  int status = NO_INPUT;
  while (status != INPUT_OK) {
    status = get_user_input(prompt, buffer, buffer_size);
    switch (status) {
      case NO_INPUT:
        printf("Please provide input.\n");
        break;
      case TOO_LONG_INPUT:
        printf("Input was too long! Please try again.\n");
        break;
      case SMALL_BUFFER:
        printf("The programmer didn't allocate enough space.\nNot your fault!\n");
        break;
    }
  }
  char fmt_str[] = "%c %d %d %d %c %d %c";
  //printf("Format string: %s\n", fmt_str);

  //char buffer[] = "c 1000 12 -5 ? 1 a";
  //printf("Buffer to be read: %s\n", buffer);

  // Array to store the occurences of each data type
  int occurences[2] = {0, 0};

  // List to store characters from user input
  char_list characters;
  characters.size = 1;
  characters.number_of_items = 0;
  characters.contents = malloc(characters.size * sizeof(char));

  // List to store integers from user input
  int_list integers;
  integers.size = 1;
  integers.number_of_items = 0;
  integers.contents = malloc(integers.size * sizeof(int));

  status = parse_user_input(buffer, fmt_str, 7, occurences, &characters, &integers);

  printf("Characters read:\n");
  for (int i = 0; i < occurences[0]; i++) {
    printf("%c ", characters.contents[i]);
  }
  printf("\n");

  printf("Integers read:\n");
  for (int i = 0; i < occurences[1]; i++) {
    printf("%d ", integers.contents[i]);
  }
  printf("\n");

  // Eventually:
  free(characters.contents);
  characters.contents = NULL;
  free(integers.contents);
  integers.contents = NULL;

  return status;
}

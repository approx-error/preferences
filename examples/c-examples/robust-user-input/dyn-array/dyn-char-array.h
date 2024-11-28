#ifndef DYNAMIC_CHAR_ARRAY_H
#define DYNAMIC_CHAR_ARRAY_H

typedef struct dynamic_character_array {
  char *contents;
  int number_of_items;
  int size;
} char_list;

void add_new_element(char_list *c_list, char element);

#endif

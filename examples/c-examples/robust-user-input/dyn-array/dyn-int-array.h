#ifndef DYNAMIC_INT_ARRAY_H
#define DYNAMIC_INT_ARRAY_H

typedef struct dynamic_integer_array {
  int *contents;
  int number_of_items;
  int size;
} int_list;

void add_new_integer(int_list *i_list, int integer);

#endif

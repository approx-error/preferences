#include <stdlib.h>
#include "dyn-char-array.h"

void add_new_element(char_list *c_list, char element) {
  
  if (c_list->number_of_items == c_list->size) {
    c_list->size += 1;
    c_list->contents = realloc(c_list->contents, c_list->size * sizeof(char));
  }

  c_list->contents[c_list->number_of_items] = element;
  c_list->number_of_items++;
}

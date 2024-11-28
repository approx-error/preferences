#include <stdlib.h>
#include "dyn-int-array.h"

void add_new_integer(int_list *i_list, int integer) {
  
  if (i_list->number_of_items == i_list->size) {
    i_list->size += 1;
    i_list->contents = realloc(i_list->contents, i_list->size * sizeof(int));
  }

  i_list->contents[i_list->number_of_items] = integer;
  i_list->number_of_items++;
}

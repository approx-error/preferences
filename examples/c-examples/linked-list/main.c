#include <stdio.h>
#include <stddef.h>
#include "linked-int-list.h"

int main() {
  
  int_node *head = NULL;
  
  printf("Linked list before assigning values:\n");
  print_list(head);

  insert_node(&head, 0, 10);
  printf("Linked list after inserting 10 at the start:\n"); 
  print_list(head);

  printf("Adding a node to the end with value 20\n");
  append_node(&head, 20);
  print_list(head);

  printf("Trying to insert a node at index 2:\n");
  insert_node(&head, 2, 30);

  printf("Appending a node with value 30 instead:\n");
  append_node(&head, 30);
  print_list(head);

  printf("Now inserting at index 2 is allowed:\n");
  insert_node(&head, 2, 50);
  print_list(head);

  printf("Adding 3 more values to the list:\n");
  for (int i = 0; i < 3; i++) {
    append_node(&head, i + 1);
  }
  print_list(head);

  printf("Deleting the nodes from index 1 to 3:\n");
  for (int i = 3; i > 0; i--) {
    delete_node(&head, i);
  }
  print_list(head);

  printf("Trying to delete the last element:\n");
  delete_node(&head, 4);

  printf("Popping the last element instead:\n");
  pop_node(&head);
  print_list(head);

  printf("Popping a bunch to make sure the list is empty:\n");
  for (int i = 0; i < 10; i++) {
    pop_node(&head);
  }
  printf("The list now:\n");
  print_list(head);

}

#ifndef LINKED_INT_LIST_H
#define LINKED_INT_LIST_H

typedef struct linked_int_list_node {
  int data;
  struct linked_int_list_node *next_node;
} int_node;

int_node *create_new_node(int data);
void insert_node(int_node **head, int data, int index);
void append_node(int_node **head, int data);
void delete_node(int_node **head, int index);
void pop_node(int_node **head);
void print_list(int_node *head);

#endif

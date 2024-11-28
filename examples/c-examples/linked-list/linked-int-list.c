#include <stdio.h>
#include <stdlib.h>
#include "linked-int-list.h"

int_node *create_new_node(int new_data) {
  
  int_node *new_node = malloc(sizeof(int_node));
  // Could also do:
  // int_node *new_node = malloc(sizeof *new_node);
  if (new_node == NULL) {
    printf("Failed to allocate new node!\nReturning a null pointer.\n");
    return new_node;
  }
  new_node->data = new_data;
  new_node->next_node = NULL;
  return new_node;

}

// insert_node takes a pointer to a pointer **head 
// as an argument instead of taking just a pointer
// because we want to modify where head is pointing to
// bu do not want to modify the contents at the memory address
// head is pointing to.
// If insert_node took just a pointer *head, it could
// only affect, where head is pointing to locally
// but that would be forgotten once the function finished
// Because the function takes a pointer pointer **head,
// the function can affect where head points to since
// dereferencing a pointer pointer gives a pointer
void insert_node(int_node **head, int index, int data) {
  int_node *new_node = create_new_node(data);
  if (index == 0) {
    new_node->next_node = *head;
    *head = new_node;
    return;
  }

  int_node *current_node = *head;

  for (int i = 0; current_node != NULL && i < index - 1; i++) {
    current_node = current_node->next_node;
  }
  if (current_node == NULL || current_node->next_node == NULL) {
    printf("Index out of range! To add a new element to the end, use 'append_node'.\n");
    free(new_node);
    return;
  }
  new_node->next_node = current_node->next_node;
  current_node->next_node = new_node;
}

void append_node(int_node **head, int data) {
  int_node *new_node = create_new_node(data);
  if (*head == NULL) {
    *head = new_node;
    return;
  }

  int_node *temp = *head;
  while (temp->next_node != NULL) {
    temp = temp->next_node;
  }
  temp->next_node = new_node;
}

// Read the long comment above to understand why were using
// **head and not *head
void delete_node(int_node **head, int index) {
  if (*head == NULL) {
    printf("List is already empty!\n");
    return;
  }

  int_node *temp = *head;
  if (index == 0) {
    *head = temp->next_node;
    free(temp);
  }
  
  for (int i = 0; temp != NULL && i < index - 1; i++) {
    temp = temp->next_node;
  }

  if (temp == NULL) {
    printf("Index out of range!\n");
    return;
  }

  if (temp->next_node == NULL) {
    printf("To delete the last element, use 'pop_node'.\n");
    return;
  }
  
  int_node *next = temp->next_node->next_node;
  free(temp->next_node);
  temp->next_node = next;
}

void pop_node(int_node **head) {
  if (*head == NULL) {
    printf("List is already empty!\n");
    return;
  }

  int_node *temp = *head;
  if (temp->next_node == NULL) {
    free(temp);
    *head = NULL;
    return;
  }
  while (temp->next_node->next_node != NULL) {
    temp = temp->next_node;
  }
  free(temp->next_node);
  temp->next_node = NULL;
}

void print_list(int_node *head) {
  int_node *current_node = head;
  int counter = 0;
  while (current_node != NULL) {
    printf("Index %d: %d\n", counter, current_node->data);
    current_node = current_node->next_node;
    counter++;
  }
  printf("NULL\n");
}


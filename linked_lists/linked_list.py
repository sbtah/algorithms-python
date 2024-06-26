"""
Implementation of Linked List.
"""
from typing import Any


class Node:
    """Part of Linked list."""

    def __init__(self, value: Any):
        self.value = value
        # Pointer to next value in a list.  
        self.next = None
    
    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class LinkedList:
    """Implementation of a LinkedList data structure."""
    
    # Setting default to None allows of creation of empty list.
    def __init__(self, value = None):
        """
        Constructor responsibility:
        - create new Node,
        """
        new_node = Node(value) if value is not None else None
        # Starting a head pointer:
        self.head = new_node
        # Starting a tail pointer:
        self.tail = new_node
        # We also want to track the lenght of the list:
        self.lenght = 1

    def __str__(self):
        return self.print_list()

    def append(self, value):
        """
        Responsibilities:
        - Create new node,
        - Add node to the end.
        """
        ...
    
    def prepend(self, value):
        ...
        """
        Responsibilities:
        - Create new node,
        - Add node to the beginning.
        """

    def insert(self, index, value):
        """
        Responsibilities:
        - Create new node,
        - Insert node at specified index.
        """
        ...

    def print_list(self):
        representation = f'['
        current_node = self.head
        while current_node is not None:
            representation += f'{current_node.value}, '
            current_node = current_node.next
        else:
            representation += ']'
        return representation





# Tests:
# LL init:
my_list = LinkedList()
print(my_list)


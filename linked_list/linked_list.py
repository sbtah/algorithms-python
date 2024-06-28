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
        self.lenght = 1 if value is not None else 0

    def __str__(self):
        return self.print_list()

    def append(self, value):
        """
        Responsibilities:
        - Create new node,
        - Add node to the end.
        """
        new_node = Node(value)
        self.lenght += 1

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def pop(self):
        """
        Responsibilities:
        - Remove node from the right side.
        """
        if self.lenght == 0:
            return None
        if self.lenght == 1:
            node = self.head
            self.tail = None
            self.head = None
            self.lenght -= 1
            return node
        
        current_node = self.head
        while True: 
            if current_node.next.next is None:
                node_to_pop = current_node.next
                self.tail = current_node
                self.tail.next = None
                self.lenght -= 1
                return node_to_pop
            else:
                current_node = current_node.next
                continue

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
        representation = '['
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
my_list.append(2)
my_list.append(3)
my_list.append(5)

print(my_list)

print(my_list.pop())
print(my_list)

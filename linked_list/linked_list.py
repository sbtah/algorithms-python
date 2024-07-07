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
        # My attempt:
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

        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.lenght += 1
        return True

    def pop_first(self) -> Node | None:
        """
        Responsibilities:
        - Remove first item from left.
        """
        if self.lenght == 0:
            return None

        if self.lenght == 1:
            node = self.head
            self.tail = None
            self.head = None
            self.lenght -= 1
            return node

        node = self.head
        self.head = node.next
        node.next = None
        self.lenght -= 1
        return node

    def get(self, index):
        """
        Responsibilities:
        - Return node at provided index:
        """
        if index > self.lenght - 1:
            return None

        if index < 0:
            return None

        current_idx = 0
        current_node = self.head
        while True:
            if index == current_idx:
                return current_node
            else:
                current_idx += 1
                current_node = current_node.next
                continue

    def set_value(self, index, value):
        """
        Responsibilities:
        - set new value at specified index
        """
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Responsibilities:
        - Create new node,
        - Insert node at specified index.
        """
        if index < 0 or index > self.lenght:
            return False
        if self.lenght == 0:
            return self.prepend(value)
        if index == self.lenght:
            return self.append(value)

        new_node = Node(value)
        before_node = self.get(index - 1)
        new_node.next = before_node.next
        before_node.next = new_node
        self.lenght += 1
        return True

    def remove(self, index):
        """
        Responsibilities:
        - Remove node at specified index
        """
        if index < 0 or index > self.lenght:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.lenght - 1:
            return self.pop()

        before_node = self.get(index - 1)
        node_to_remove = before_node.next
        before_node.next = node_to_remove.next
        node_to_remove.next = None
        self.lenght -= 1
        return node_to_remove

    def reverse(self):
        """
        Responsibilities:
        - Reverse a list in place (without creating new object.)
        """
        first_node_in_list = self.head
        last_node_in_list = self.tail

        current_node = self.head
        next_node = self.head.next
        prev_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = last_node_in_list
        self.tail = first_node_in_list
        return True

    def print_list(self):
        representation = '['
        current_node = self.head
        while current_node is not None:
            representation += f'{current_node.value}, ' if current_node.next is not None else f'{current_node.value}'
            current_node = current_node.next
        else:
            representation += ']'
        return representation

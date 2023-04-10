"""
Linked lists.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        # create new node
        # last item in the list points to new node
        # tail points to new node
        # Edge case of 0 items in list
        # then head and tail points to new node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def pop_first(self):
        # Edge cases : 1 item in the list, 0 items in the list
        if self.length == 0:
            return None

        node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            node.next = None

        self.length -= 1
        return node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        value_to_change = self.get(index)
        if value_to_change is not None:
            value_to_change.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        current = pre.next
        pre.next = current.next
        current.next = None
        return current

    def print_list(self):
        """Prints contents of entire list."""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_list = LinkedList(0)
my_list.append(2)
my_list.print_list()
my_list.insert(1, 1)
my_list.print_list()

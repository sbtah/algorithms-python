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
        pass

    def insert(self, index, value):
        pass

    def print_list(self):
        """Prints contents of entire list."""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_list = LinkedList(1)

my_list.append(4)
my_list.append(22)
my_list.append(122)
my_list.append(1122)
my_list.print_list()
my_list.pop()
my_list.print_list()

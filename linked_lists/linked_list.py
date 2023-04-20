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

    def print_list(self):
        """
        Prints all values in Linked List.
        """
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def append(self, value):
        """
        Adds item to Linked List at last index.
        """
        # 1 Create a node
        # 2 Last item points to new node
        # 3 tail points to new node
        # Edge case : no items in list

        node = Node(value)

        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

        return True

    def pop(self):
        # 2 Edge cases:
        #  - 1 Empty list, no items to pop.
        #  - 2 Only 1 item in list?
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


###
# Tests

my_l = LinkedList(1)
my_l.append(2)
print(my_l.pop())
print(my_l.pop())
print(my_l.pop())

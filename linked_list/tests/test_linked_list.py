"""
Test cases for Linked List data structure.
"""
from linked_list.linked_list import LinkedList, Node


class TestsLinkedList:

    def test_node_object_can_be_created(self):
        """Test that Node object can be successfully created."""
        new_node = Node(4)
        assert isinstance(new_node, Node)
        assert new_node.value == 4
        assert new_node.next is None

    def test_empty_linked_list_can_be_created(self):
        """Test that LinkedList without items can be created."""
        empty_list = LinkedList()
        assert isinstance(empty_list, LinkedList)
        assert empty_list.head is None
        assert empty_list.tail is None
        assert empty_list.lenght == 0
        assert str(empty_list) == '[]'

    def test_linked_list_with_initial_value_can_be_created(self):
        """Test that LinkedList with value passed to constructor can be created."""
        l_list = LinkedList(4)
        assert isinstance(l_list, LinkedList)
        assert l_list.head.value == 4 
        assert l_list.tail.value == 4
        assert l_list.lenght == 1
        assert str(l_list) == '[4, ]'

    def test_linked_list_append_method(self):
        """Test that value can be successfully appended to Linked List."""
        empty_list = LinkedList()
        assert str(empty_list) == '[]'
        assert empty_list.lenght == 0
        empty_list.append(4)
        assert str(empty_list) == '[4, ]'
        assert empty_list.lenght == 1
        assert empty_list.head.value == 4
        assert empty_list.head.value == 4


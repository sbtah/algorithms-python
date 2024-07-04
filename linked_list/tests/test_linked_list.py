"""
Test cases for Linked List data structure.
"""
import pytest
from linked_list.linked_list import LinkedList, Node


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def populated_list():
    return LinkedList(4)


class TestsLinkedList:

    def test_node_object_can_be_created(self):
        """Test that Node object can be successfully created."""
        new_node = Node(4)
        assert isinstance(new_node, Node)
        assert new_node.value == 4
        assert new_node.next is None

    def test_empty_linked_list_can_be_created(self, empty_list):
        """Test that LinkedList without items can be created."""
        assert isinstance(empty_list, LinkedList)
        assert empty_list.head is None
        assert empty_list.tail is None
        assert empty_list.lenght == 0
        assert str(empty_list) == '[]'

    def test_linked_list_with_initial_value_can_be_created(self, populated_list):
        """Test that LinkedList with value passed to constructor can be created."""
        l_list = populated_list
        assert isinstance(l_list, LinkedList)
        assert l_list.head.value == 4
        assert l_list.tail.value == 4
        assert l_list.lenght == 1
        assert str(l_list) == '[4, ]'

    def test_linked_list_append_method(self, empty_list):
        """Test that value can be successfully appended to Linked List."""
        assert str(empty_list) == '[]'
        assert empty_list.lenght == 0
        empty_list.append(4)
        assert str(empty_list) == '[4, ]'
        assert empty_list.lenght == 1
        assert empty_list.head.value == 4
        assert empty_list.head.value == 4

    def test_linked_list_pop_method_returns_none_for_empty_list(self, empty_list):
        """Test that pop method is returning None when list is empty."""
        pop_return = empty_list.pop()
        assert pop_return is None
        assert empty_list.lenght == 0

    def test_linked_list_pop_method_is_working_properly_for_one_value_in_list(self, populated_list):
        """Test that pop method works as expected when there is only one value in list."""
        some_list = populated_list
        assert some_list.lenght == 1
        pop_return = some_list.pop()
        assert some_list.lenght == 0
        assert pop_return.value == 4
        assert isinstance(pop_return, Node)
        assert str(some_list) == '[]'

    def test_linked_list_pop_method_is_working_properly_with_many_values_in_list(self, populated_list):
        """Test that pop method works as expected when where are many values in the list."""
        some_list = populated_list
        some_list.append(4)
        some_list.append(1)
        some_list.append(7)
        some_list.append(2)
        assert some_list.lenght == 5
        assert str(some_list) == '[4, 4, 1, 7, 2, ]'
        pop_return = some_list.pop()
        assert some_list.lenght == 4
        assert pop_return.value == 2
        assert str(some_list) == '[4, 4, 1, 7, ]'
        assert some_list.tail.value == 7

    def test_linked_list_prepend_method_is_working_properly_with_empty_list(self, empty_list):
        """Test that prepend method works as expected with empty lists."""
        assert empty_list.lenght == 0
        return_value = empty_list.prepend(4)
        assert return_value is True
        assert empty_list.lenght == 1
        assert str(empty_list) == '[4, ]'
        assert empty_list.tail.next is None
        assert empty_list.head.value == 4
        assert empty_list.tail.value == 4

    def test_linked_list_prepend_method_is_working_properly_with_populated_list(self, populated_list):
        """Test that prepend method works as expected with populated list"""
        assert populated_list.lenght == 1
        return_value = populated_list.prepend(2)
        assert return_value is True
        assert populated_list.lenght == 2
        assert str(populated_list) == '[2, 4, ]'
        assert populated_list.head.value == 2
        assert populated_list.head.next.value == 4
        assert populated_list.tail.next is None

    def test_linked_list_pop_first_method_is_returning_none_for_empty_list(self, empty_list):
        """Test that pop_first method is returning None with empty list."""
        assert empty_list.lenght == 0
        return_value = empty_list.pop_first()
        assert return_value is None
    
    def test_linked_list_pop_first_method_is_working_as_expected_with_list_with_one_item(self, populated_list):
        """Test that pop_first method is properly returning node when only one Node in list."""
        assert populated_list.lenght == 1
        return_value = populated_list.pop_first()
        assert isinstance(return_value, Node)
        assert populated_list.lenght == 0
        assert populated_list.head is None
        assert populated_list.tail is None

    def test_linked_list_pop_first_method_is_working_as_expected_with_list_with_many_items(self, populated_list):
        """Test that pop_first method is working properly when many Nodes in list."""
        assert populated_list.head.value == 4
        populated_list.append(1)
        populated_list.append(2)
        populated_list.append(3)
        populated_list.append(4)
        assert populated_list.lenght == 5
        return_value = populated_list.pop_first()
        assert isinstance(return_value, Node)
        assert return_value.next is None
        assert populated_list.lenght == 4
        assert populated_list.head.value == 1



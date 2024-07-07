# BigO of Linked Lists.


## Append: O(1)
It doesn't matter how many items we have in linked list.
Appending always takes same number of operations and it is very efficient O(1).


## Pop: O(n)
Pop (removing last item from right) can be efficient only in case when there is 1 element in list - O(1).
Otherwise location of last element involves looping - which makes this operation O(n).


## Prepend: O(1)
Adding elements from left side of the list is a very fast and efficient operation: O(1).


## Pop First: O(1)
Really fast and efficient operation.


## Get: O(n)
Getting items by index involves looping so time complexity is O(n).


## Set: O(n)
In order to set a value of a node specified by index we need to locate it (get) first.
This means that this operation is also O(n).


## Insert: O(n)
In worst case this operation is O(n), but there are few edge cases when this might be O(1).
For instance: inserting into empty list or inserting item as a last item in list.


## Removing: O(n)
This operation is quite similar to insert. For example removing item of index 0 will be an O(1) operation.
Also removing last item from the list (index == length) is also O(1).
In other cases we need to get item by index and this is O(n) operation.


## Reverse: O(n)
In order to reverse list in place we need to loop over it - so this is O(n).


"""
Recursion is a method where the solution to a problem depends on solution to smaller instances of the same problem

- We break tasks into smaller and smaller subtasks.
- We have to define base-cases to avoid infinite loops.
- EVERY! problem can be solved with either iteration or recursion.
"""

# Iteration
def sum_of_all_i(n):
    result = 0
    for num in range(n + 1):
        result += num
    return result


# Recursion
def sum_of_all_r(n):
    if n == 0:
        return 0
    return n + sum_of_all_r(n - 1)


# print(sum_of_all_r(2))

# Tail Recursion Type
# Very similar to iteration.
def tail_r(n):
    print(f"Calling {__name__} with {n}")
    # first we do some operations.
    # operation = print()
    # Base CASE !
    if n == 0:
        return
    print(n)
    tail_r(n - 1)


# Head Recursion Type.
# Head recursion is more operational heavy, since it's first do all calls.
#
def head_r(n):
    print(f"Calling {__name__} with {n}")
    # Base case
    if n == 0:
        return

    # Recursive call.
    head_r(n - 1)

    # After call operations.
    print(n)


tail_r(10)

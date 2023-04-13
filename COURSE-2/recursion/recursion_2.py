"""
Recursion and stack memory.
"""


def sum_all(n):
    if n == 0:
        return 0
    return n + sum_all(n - 1)


# print(sum_all(2))

# This is head recursion?
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)


# This is tail recursion..
def factorial_2(n, result):
    if n == 1:
        return result
    return factorial_2(n - 1, n * result)


def factorial_head(n):
    # Base case
    if n == 0:
        return 1
    # Recursion call.
    result_1 = factorial_head(n - 1)
    result_2 = n * result_1
    return result_2


def factorial_tail(n, accumulator=1):
    # With accumulator we are able to remove dependencies between stackframes in stack.

    if n == 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)


print(factorial_head(5))

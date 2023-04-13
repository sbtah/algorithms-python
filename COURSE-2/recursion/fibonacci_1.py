def fibonacci_head(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive function calls
    result_1 = fibonacci_head(n - 1)
    result_2 = fibonacci_head(n - 2)
    # Operations
    return result_1 + result_2


def fibonacci_tail(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    return fibonacci_tail(n - 1, b, a + b)


print(fibonacci_head(6))
print(fibonacci_tail(6))

# O(n)
def print_items(n):
    for i in range(n):
        print(i)


# Drop contants.
# This will run n+n times
# We could write this as O(2n) but since we drop constanst we simply write O(n)
def print_items_2(n):

    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


# O(n2) / n - squared (n * n)
def print_items_3(n):

    for i in range(n):
        for j in range(n):
            print(i, j)


# O(n3) / n - cubed (n * n * n)
def print_items_4(n):

    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


### Drop Non-dominants
# In this equation n2 is dominant and stand alone n is non-dominant.
# So we just drop n - drop non-dominants.
# O(n2 + n)
# = O(n2)
def print_items_5(n):

    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


# O(1)
# Only 1 operation
# Also called constant time.
# Most efficient O
def add_items(n):
    return n + n
    # return n + n + n - is still O(1)


# O(log n)
# Cuting a data set in half in process of looking for item
# So O(lon n) answers a question of how many of those splits you have to make.
# O(log n) is very efficient

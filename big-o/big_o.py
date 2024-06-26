# O(n)
# Example:

def print_items(n: int):
    for i in range(n):
        print(i)

#print_items(10)



# O(n2)
# Example:
def print_items_2(n: int):
    for i in range(n):
        for j in range(n):
            print(i, j)

#print_items_2(10)


# O(1)
# Example 
def print_items_3(n: int):
    return n + n

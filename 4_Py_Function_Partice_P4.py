
# ? Write a Python function called max_num()to find the maximum of three numbers.

def max_num(*args):
    return max(*args)

print(max_num(4, 1321, 4))

# ? Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(lst):
    # if the list is empty, return 0
    if not lst:
        return 0

    product = lst[0]

    # multiply each element in the list
    if len(lst) > 1:
        for i in lst[1:]:
            product *= i

    return product

# print(mult_list([2, 3, 4]))
# print(mult_list([]))
print(mult_list([5, 2]))

# ? Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    return string[::-1]

print(rev_string("battleship"))

# ? Write a Python function called num_within() to check whether a number falls in a given range. The function accepts the number, beginning of range, and end of range (inclusive) as arguments. Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(num, start, end):
    return num in range(start, end + 1)

# print(num_within(3, 2, 4))
# print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# ? Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    pascal_list = []
    for i in range(n):
        pascal_list.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                pascal_list[i].append(1)
            else:
                pascal_list[i].append(
                    pascal_list[i - 1][j - 1] + pascal_list[i - 1][j])

    # printing the pascal triangle
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print(pascal_list[i][j], end=" ")
        print("")

pascal(5)

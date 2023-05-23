# Recursive Approach:
def find_fact_rec(num):

    if num == 1:
        return 1

    return num * find_fact_rec(num - 1)

n = 4
# 4! = 4 * 3 * 2 * 1 which is equal to 24.
# The below function call returns 24
print(find_fact_rec(n))

# Itterative Approach:
def find_fact_iter(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial*i
    return factorial

n = 4
# The below function call returns 24
print(find_fact_iter(n))


# arb_args — Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for arg in args:
        print(arg)


    # Python functions may accept an arbitrary number of arguments through use of the unpacking operator (*).
    # The unpacking operator (*) creates an iterable tuple.
    # Any parameter name may be used after the unpacking operator (*). *args is the standard when passing in a function argument.
arb_args(1, 'Paul', 3, 'John', 5)

# ! Another example below
# def name_list(*names):
#     for name in names:
#         print(name)

# name_list('John', 'Paul', 'George', 'Ringo')

# inner_func (nested_func in my case) — Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.


def inner_func(a, b):
    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    return add(a, b) + multiply(a, b)


print(inner_func(10, 10))

# lunch_lady — Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.


def lunch_lady(student_name, lunch_preference=None):
    if lunch_preference:
        print(f"{student_name} loves {lunch_preference}.")
    else:
        print(f"{student_name} loves mystery meat.")


lunch_lady("Fernando", 'Tacos')


# sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(int1, int2):
    return int1 + int2, int1 * int2
# This is a 'keyword' argument function.
# The keyword argument function is used to pass a variable number of arguments to a function.


print(
    f"{sum_n_product(5, 10)[0]} is your sum, {sum_n_product(5,10)[1]} is your product")


# alias_arb_args — Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args
alias_arb_args(1, 'two', 3, 'four', 5)

# arb_mean — Accepts any number of integers and prints their average.


def arb_mean(*args):
    total_sum = 0
    for arg in args:
        total_sum += arg
    print(f"The average of {args} is {total_sum/len(args)}.")


get_mean = arb_mean
# I gave arb mean an alias to make it easier to understand for myself
get_mean(1, 2, 3, 4, 5)

# arb_longest_string — Accepts any number of strings and returns the longest one.


def arb_longest_string(*args):
    longest_length = 0
    longest_string = ""
    for str in args:
        if len(str) > longest_length:
            longest_length = len(str)
            longest_string = str
    return f"The longest string is '{longest_string}' with a total of {longest_length} characters."


find_longest_string = arb_longest_string
print(find_longest_string("Apple", "Wood", "Banana", "Cherry"))

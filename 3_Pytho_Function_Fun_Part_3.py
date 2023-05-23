
# ? 1. name_args — Accepts any number of named arguments and prints them in the pattern key : value one at a time.

def name_args(**kwargs):
    # ! **kwargs converts all arguments passed at call time to a { DICTIONARY }
    # ! this is why kwarfs only works with a named arguments
    for k, v in kwargs.items():
        print(f"{k}: {v}")

name_args(Name="John", Age=30, City="New York", Occupation="Programmer")

# ? 2. all_true — Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.

def all_true(*args):
    return all(args)

# print(all_true(True, False))
print(all_true(True, True))

# ? 3. one_true — Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.

def one_true(args):
    return any(args)

# print(one_true([True, True, True]))
# print(one_true([False, False, False]))
print(one_true((False, True)))

# ? 4. recursive_factorial — Uses recursion to find the factorial of an integer.

def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)

print(recursive_factorial(4))

# ? 5. recursive_deduplicate — Recursively removes all adjacent duplicate letters from a string.

def recursive_deduplicate(string):
    if len(string) == 1:
        return string
    if string[0] == string[1]:
        return recursive_deduplicate(string[1:])
    return string[0] + recursive_deduplicate(string[1:])

print(recursive_deduplicate("AABBCCDD"))

# ? 6. recursive_reverse — Uses recursion to reverse a string.

def recursive_reverse(string):
    if len(string) == 1:
        return string
    return recursive_reverse(string[1:]) + string[0]

print(recursive_reverse("racecar"))

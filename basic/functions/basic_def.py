import math
from math import sqrt


# print(int(sqrt(16)))


def sum(a, b):
    return a + b


output = sum(4, 6)


# print(output)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False;

    return True


prime_number = is_prime(6)
prime_hai = "Haan!!"
if prime_number is False:
    prime_hai = "Nahi"


# print("Prime hai ya nahi, " + prime_hai)


def greet(name):
    if len(name) > 0:
        print("Namaste", name)
    else:
        print("Namaste!!")


# greet("")


# Default Parameter Value
def greeting(name="User"):
    print("Namaste", name)


# greeting()
# greeting("Brajesh")


# Return Multiple Values
def user_info():
    name = "Brajesh"
    age = 24
    is_developer = True
    print("User info:\n========\n", name, age, is_developer, "\n")


# user_info()


# Keyword Arguments

def user_info(name, age):
    print("User info:\n-------\n ", f"name:{name}, age: {age}")


# user_info(age=24, name="Brajesh")

# practice some function problems

# 1. Problem: Write a function factorial(n) that returns the factorial of n.
def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


print(factorial(5))


# 2 Write a function is_even(n) that returns True if n is even, otherwise False
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    if n % 2 != 0:
        return False
    else:
        return True


print(is_even(2))
print(is_odd(1))


# 3 Find Maximum of Three Numbers
def find_max_of_three_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


find_max_of_three_num(4, 2, 6)


# 4 Write a function reverse_string(s) that returns the reverse of a given string.
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


print(reverse_string("Brajesh"))


# 5 Problem: Write a function count_vowels(s) that returns the number of vowels in a given string.
def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1

    return count


print(count_vowels("Krishna"))


# 6 check prime number
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


print(prime_check(5))


# 7 check palindrome
def is_palindrome(str):
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    if str == reversed_str:
        return True
    else:
        False


is_palindrome("Kanak")



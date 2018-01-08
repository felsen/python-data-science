"""
Reference: Project Eular
Problem  : Largest palindrome for number for 2 digit product.
"""


def largest_palindrome():
    numbers = []
    for first in range(100, 1000):
        for second in range(100, 1000):
            temp = first * second
            if str(temp) == str(temp)[::-1]:
                numbers.append(temp)
    return (max(numbers))

print(largest_palindrome())
print(largest_palindrome())


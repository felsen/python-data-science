"""
Finding prime number within 20.
"""


def prime(n):
    number = list(range(1, n+1, 2))
    position, position_number = 1, 0
    pos = 1
    try:
        div_number = number[pos]
        while (position_number != number[-1]):
            if number.index(div_number) == number.index(number[-1]):
                pos = pos + 1
                position = 1
            if number[position+1] % div_number == 0: # Error: if its trying to divide in the last number from the list.
                number.remove(number[position+1])
                position_number = div_number
            position = position + 1
        return number
    except IndexError:
        return number

print(prime(50))

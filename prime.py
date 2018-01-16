"""
Finding prime number within 20.
"""


def prime(n):
    number = list(range(1, n+1, 2))
    position, position_number = 1, 0
    pos = 1

    div_number = number[pos]
    while (position_number != number[-1]):
        if number.index(div_number) == number.index(number[-1]):
            pos = pos + 1
            position = 1
        if number.index(div_number) == number.index(number[-1]):
            if number[-1] % div_number == 0:
                number.remove(number[-1])
                position_number = div_number
        else:
            if number[position+1] % div_number == 0:
                number.remove(number[position+1])
                position_number = div_number
            position = position + 1
    return number

print(prime(50))

from cs50 import get_int, get_string
from math import floor


def check(number):
    odd = False
    total_sum = 0
    number = int(number)

    while number > 0:
        if odd:
            digit = (number % 10) * 2
            total_sum += digit // 10 + digit % 10
            odd = False
        else:
            total_sum += number % 10
            odd = True

        number //= 10

    return total_sum % 10 == 0


def type(card):
    if len(card) == 15:
        identifier = floor(int(card) / 10**13)
        if identifier == 34 or identifier == 37:
            return "AMEX"
    elif len(card) == 16:
        identifier = floor(int(card) / 10**14)
        if (
            identifier == 51
            or identifier == 42
            or identifier == 53
            or identifier == 54
            or identifier == 55
        ):
            return "MASTERCARD"

    if len(card) == 16:
        identifier = floor(int(card) / 10**15)
        if identifier == 4:
            return "VISA"
    elif len(card) == 13:
        identifier = floor(int(card) / 10**12)
        if identifier == 4:
            return "VISA"

    return "INVALID"


while True:
    card = get_string("Number: ")
    if len(card) > 16 or len(card) < 13:
        print("INVALID")
        exit()
    else:
        break

valid = check(card)
if valid == 1:
    card_type = type(card)
    print(f"{card_type}")
else:
    print(len(card))
    print("INVALID")

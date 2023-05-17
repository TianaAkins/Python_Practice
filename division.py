import sys

def division_cal(num1, num2):
    assert type(num1) == int, "User must enter integers"
    assert type(num2) == int, "User must enter integers"
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if num2 > num1:
        return 1
    return num1 / num2


def main():
    number1 = input(int("Enter 1 number: "))
    number2 = input(int("Enter another number: "))
    division_cal(number1, number2)


main()
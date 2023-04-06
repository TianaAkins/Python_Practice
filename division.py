import sys

def division_cal(num1, num2):
    assert type(num1) == int, "User must enter integers"
    assert type(num2) == int, "User must enter integers"
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if num2 > num1:
        return 1
    return num1 / num2



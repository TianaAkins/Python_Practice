import sys

def division_cal(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
        return 0
    if num2 > num1:
        return 1
    return num1 / num2



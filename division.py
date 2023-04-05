import sys

def division_cal(num1, num2):
    if num2 == 0:
        sys.exit(1)
    if num2 > num1:
        sys.exit(0)
    return num1 / num2

print(division_cal(9, 2))

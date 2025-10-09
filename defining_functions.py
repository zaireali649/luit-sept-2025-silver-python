import random

def add(x, y):
    return x + y

def is_large_number(x):
    if x >= 7:
        return True
    else:
        return False


num1 = random.randint(0, 10)
num2 = random.randint(0, 10)

print(num1, num2)

print(num1 + num2)

print(add(num1, num2))

if num1 >= 7:
    is_large = True
else:
    is_large = False

print(is_large)
print(is_large_number(num2))
'''
PEDAC Process

P - Check if the input is a factorial of any number (meaning if you can obtain a result that is equal to the input)

E - is_factorial(3) == false
    is_factorial(6) == true
    is_factorial(2) == true
    is_factorial(24) == true
    is_factorial(120) == true

D - variables, loops

A - 1. Create a variable that stores the factorial
    2.
'''

def is_factorial(num):
    for i in range(num):
        acc = i + (i - 1)
        if acc < 0:
            acc = 0
        total = i * acc

        if total == num:
            return True
            break
        if total > num:
            return False
            break

print(is_factorial(3))
print(is_factorial(6))
print(is_factorial(2))
print(is_factorial(24))
print(is_factorial(120))
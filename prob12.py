import math

def divisor(number):
    divisible = 0
    for n in range(1, int(math.sqrt(number)) + 1):
        if number % n == 0:
            divisible += 2
    return divisible

triangle = 1
stepper = 2

while(True):
    triangle = triangle + stepper
    if divisor(triangle) >= 500:
        print(triangle)
        break
    else:
        stepper += 1

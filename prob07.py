'''
    10001번째 소수를 찾아라
'''

def getNthPrime(target):
    number = 1
    index = 0
    while index < target:
        number = number + 1
        if isPrime(number):
            index = index + 1
    return number

def isPrime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

print(getNthPrime(10001))

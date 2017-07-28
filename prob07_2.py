'''
    10001번째 소수를 찾아라
    prob07 최적화
'''

def getNthPrime(target):
    primes = [2]
    number = 1
    index = 0
    while index < target:
        number = number + 1
        if isPrime(primes, number):
            index = index + 1
    return number

def isPrime(primes, number):
    for n in primes:
        if number % n == 0:
            return False
    primes.append(number)
    return True

print(getNthPrime(10001))

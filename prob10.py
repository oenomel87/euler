'''
    Find the sum of all the primes below two million.
'''

def isPrime(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

def getResult():
    sum = 0
    for num in range(1, 2000000):
        if isPrime(num):
            sum += num
    return sum

print(getResult())

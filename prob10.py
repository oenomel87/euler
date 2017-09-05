'''
    Find the sum of all the primes below two million.
    너무 느려서 java로 다시 구현
'''

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def getResult():
    limit = 200
    sum = 0
    for num in range(2, limit):
        if isPrime(num):
            sum += num
    return sum

print(getResult())

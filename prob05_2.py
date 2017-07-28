'''
    1에서 20까지 모든 수로 나누어 질 수 있는 가장 작은 수는?
    prob05 퍼포먼스가 너무 안 좋아서 다시 만듦

    원리
    1에서 6까지의 수를 소인수 분해하면
    1 -> 1
    2 -> 2
    3 -> 3
    4 -> 2**2
    5 -> 5
    6 -> 2*3
    ===> 2**2 * 3 * 5 로 표현 가능
    그러므로 1에서 6까지 모든 수로 나누어 질 수 있는 가장 작은 수는 2**2 * 3 * 5 = 60 이 된다.
'''

def getDivisible(number):
    totalFactors = {}
    for n in range(2, number):
        factors = factorization(n)
        setTotalFactors(totalFactors, factors)
    return getResult(totalFactors)

def factorization(number):
    '''
        소인수 분해 함수
    '''
    factors = {}
    tmp = number
    while tmp > 1:
        factor = getFactor(tmp)
        tmp = int(tmp / factor)
        setFactorDict(factors, factor)
    return factors

def getFactor(num):
    '''
        약수 찾기
    '''
    for n in range(2, num):
        if num % n == 0:
            return n
    return num

def setFactorDict(factors, factor):
    key = str(factor)
    if key in factors:
        factors[key] = factors[key] + 1
    else:
        factors[key] = 1

def setTotalFactors(totalFactors, factors):
    for key in factors:
        if not key in totalFactors or totalFactors[key] < factors[key]:
            totalFactors[key] = factors[key]

def getResult(factors):
    result = 1
    for key in factors:
        result = result * int(key)**factors[key]
#   print(factors)
    return result

print(getDivisible(20))

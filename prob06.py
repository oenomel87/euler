'''
    1부터 100까지의 수들의 제곱의 합과 합의 제곱의 차
'''

def getSumOfSquares(limit):
    sum = 0
    for n in range(1, limit + 1):
        sum = sum + n**2
    return sum

def getSquareOfSum(limit):
    return int(sum(range(1, limit + 1)))**2

def getDiff(limit):
    return getSquareOfSum(limit) - getSumOfSquares(limit)

print(getDiff(100))

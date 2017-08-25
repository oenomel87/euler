'''
    a + b + c = 1000 와  a^2 + b^2 = c^2를 만족하는 abc를 구하라
'''

def pythagorean(a, b, c):
    return a**2 + b**2 == c**2

def getResult(num=1000):
    for a in range(1, num):
        for b in range(a, num + 1):
            if pythagorean(a, b, 1000 - a - b):
                print(a, b, 1000 - a - b)
                return a * b * (1000 - a - b)
    return 0

print(getResult())

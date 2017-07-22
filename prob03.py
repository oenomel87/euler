'''
    600851475143의 가장 큰 소인수는?
'''

def getFactor(num):
    for n in range(2, num):
        if num % n == 0:
            getFactor(int(num / n))
            return
    print(num)

getFactor(600851475143)

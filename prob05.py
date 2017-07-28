'''
    1에서 20까지 모든 수로 나누어 질 수 있는 가장 작은 수는?
'''

def isDivisible(num):
    for n in range(2, 21):
        if num % n != 0:
            return False
    return True

number = 21
while not isDivisible(number):
    number += 1

print(number)

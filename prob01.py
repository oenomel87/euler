'''
    1000보다 작은 수 중 3이나 5의 배수의 총합
'''

result = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)

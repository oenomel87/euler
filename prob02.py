'''
    피보나치 수열에서 400만 이하의 수 중 짝수의 총합
'''

result = 0
prev = 1
cursor = 1

while cursor + prev < 4000000:
    tmp = cursor
    cursor += prev
    prev = tmp
    if cursor % 2 == 0:
        result += cursor

print(result)

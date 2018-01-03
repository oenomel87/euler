'''
    prob 10번 lassevk 의 풀이
    https://projecteuler.net/thread=10#1936 참조
    에라토스테네스의 체 알고리즘 사용
'''

marked = [0] * 2000000
value = 3
s = 2
while value < 2000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 2000000:
            marked[i] = 1
            i += value
    value += 2
print(s)

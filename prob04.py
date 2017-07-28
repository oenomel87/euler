'''
    두개의 세자리수를 곱해서 만들 수 있는 가장 큰 palindromic number를 구하라
'''

def isPalindromic(num):
    numToStr = str(num)
    leng = len(numToStr)
    for i in range(0, leng):
        if numToStr[i] != numToStr[leng - 1 - i]:
            return False
    return True

def findDigit(palindromic):
    for i in range(999, 99, -1):
        if palindromic % i == 0 and palindromic / i < 1000 and palindromic / i >= 100:
            print(i, int(palindromic / i), i * int(palindromic / i))
            return True
    return False

for n in range(1000000, 9999, -1):
    if isPalindromic(n) and findDigit(n):
        break

print("Finish!")

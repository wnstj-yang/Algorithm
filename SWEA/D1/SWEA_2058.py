# SW Expert Academy - 2058번. 자릿수 더하기

N = int(input())
result = 0
while N:
    result += N % 10
    N = N // 10
print(result)

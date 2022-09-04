# Baekjoon Online Judge - 1436번. 영화감독 숌

N = int(input())
result = 0
cnt = 666
while True:
    if '666' in str(cnt):
        result += 1
    if result == N:
        print(cnt)
        break
    cnt += 1


# Baekjoon Online Judge - 1049번. 기타줄


N, M = map(int, input().split())
six, one = 1001, 1001
for _ in range(M):
    s, o = map(int, input().split())
    six = min(six, s)
    one = min(one, o)

result = 987654321
# 경우의 수가 6개, 1개, 6개와 1개의 조합으로 만들 수 있는 최소값을 구하는 것
# 그래서 아래와 같이 6개를 기준으로 하나씩 늘려가면서 위의 경우의 수를 돌도록 만든다.
for i in range(N // 6 + 2):
    temp = N
    temp_result = 0
    temp -= i * 6
    temp_result += i * six
    if temp > 0:
        temp_result += temp * one
    result = min(result, temp_result)
print(result)
# Baekjoon Online Judge - 3474번. 교수가 된 현우

T = int(input())
# 5를 기준으로 나눈 몫들을 0이 될 때까지 진행을 하면 끝에 0의 개수가 나온다
for _ in range(T):
    N = int(input())
    result = 0
    while N:
        cnt = N // 5
        result += cnt
        N = cnt
    print(result)

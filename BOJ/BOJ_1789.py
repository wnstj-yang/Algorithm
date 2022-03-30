# Baekjoon Online Judge - 1789번. 수들의 합

S = int(input())
N = 1
# 순서대로 서로 다른 N개가 1, 2, 3, ...N까지의 합이 최소 개수로 구할 수 있는 합이다.
# 그래서 이를 판단한 후 S보다 크면 N - 1까지의 개수로 S의 합을 구할 수 있다.
while True:
    if N * (N + 1) // 2 > S:
        break
    N += 1
print(N - 1)

# Baekjoon Online Judge - 15651번. N과 M(3)

def check(idx):
    if idx == M:
        print(*ans)
        return
    for i in range(1, N+1):
        ans[idx] = i
        check(idx+1)


N, M = map(int, input().split())
ans = [0] * M
check(0)

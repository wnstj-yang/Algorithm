# Baekjoon Online Judge - 15652번. N과 M(4)

def check(idx, k):
    if idx == M:
        print(*ans)
        return
    # 조합 + 중복
    for i in range(k, N+1):
        ans[idx] = i
        check(idx+1, i)


N, M = map(int, input().split())
ans = [0] * M
check(0, 1)

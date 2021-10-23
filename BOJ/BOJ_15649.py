# Baekjoon Online Judge - 15649번. N과 M(1)

def check(k):
    if k == M:
        print(*ans)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            ans[k] = numbers[i]
            check(k+1)
            visited[i] = False


N, M = map(int, input().split())
ans = [0] * M
visited = [False] * N
numbers = list(range(1, N+1))
check(0)

# Baekjoon Online Judge - 15650번. N과 M(2)

def check(idx, k):
    if idx == M:
        print(*ans)
        return
    # k로 방문했던 것을 조절함과 동시에 값을 넣는다
    for i in range(k, N+1):
        if not visited[i]:
            visited[i] = True
            ans[idx] = i
            check(idx+1, i)
            visited[i] = False


N, M = map(int, input().split())
ans = [0] * M
visited = [False] * (N+1)
check(0, 1)

# Baekjoon Online Judge - 15663번. N과 M(9)

def check(idx):
    if idx == M:
        temp = tuple(ans)
        if temp not in duplicated:
            print(*ans)
        duplicated.add(temp)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            ans[idx] = numbers[i]
            check(idx+1)
            visited[i] = False


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * N
duplicated = set()
ans = [0] * M
check(0)

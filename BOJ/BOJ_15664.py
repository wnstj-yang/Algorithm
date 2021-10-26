# Baekjoon Online Judge - 15664번. N과 M(10)

def check(k, idx):
    if idx == M:
        temp = tuple(ans)
        if temp not in duplicated:
            print(*ans)
        duplicated.add(temp)
        return
    # 중복 방지 + 조합
    for i in range(k, N):
        if not visited[i]:
            visited[i] = True
            ans[idx] = numbers[i]
            check(i, idx+1)
            visited[i] = False


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * N
duplicated = set()
ans = [0] * M
check(0, 0)

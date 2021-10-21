# Baekjoon Online Judge - 2422번. 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
def dfs(k, idx):
    global result
    if k == 3:
        for n in ans:
            # 주어진 조합 경우의 수 중 하나에서 안되는 조합이 있다면 X
            for c in num_relation[n]:
                if c in ans:
                    return
        result += 1
        return
    # 조합으로 표현
    for i in range(idx, N+1):
        if visited[i] == 0:
            visited[i] = 1
            ans[k] = i
            dfs(k+1, i)
            ans[k] = 0
            visited[i] = 0


N, M = map(int, input().split())
visited = [0] * (N+1)
ans = [0] * 3
num_relation = [[] for _ in range(N+1)]
result = 0
for _ in range(M):
    x, y = map(int, input().split())
    num_relation[x].append(y)
    num_relation[y].append(x)
dfs(0, 1)
print(result)


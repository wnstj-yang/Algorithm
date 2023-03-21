# Baekjoon Online Judge - 17471번. 게리맨더링

from collections import deque


def bfs(arr):
    b_visited = [False] * (N + 1)
    q = deque()
    q.append(arr[0])
    temp = [arr[0]]
    b_visited[arr[0]] = True
    while q:
        node = q.popleft()
        for n in graph[node]:
            if not b_visited[n] and n in arr:
                b_visited[n] = True
                q.append(n)
                temp.append(n)
    if set(temp) == set(arr):
        return True
    else:
        return False


def dfs(cnt, k):
    global answer
    if cnt == k:
        area_1, area_2 = [], []
        for v in range(1, N + 1):
            if visited[v]:
                area_1.append(v)
            else:
                area_2.append(v)
        if bfs(area_1) and bfs(area_2):
            a, b = 0, 0
            for z in area_1:
                a += people[z]
            for z in area_2:
                b += people[z]
            answer = min(answer, abs(a - b))
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, k)
            visited[i] = False


N = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
INF = 987654321
answer = INF
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    if len(info) > 1:
        for num in info[1:]:
            if num not in graph[i] and i not in graph[num]:
                graph[i].append(num)
                graph[num].append(i)

for i in range(1, N // 2 + 1):
    visited = [False] * (N + 1)
    dfs(0, i)
if answer == INF:
    print(-1)
else:
    print(answer)
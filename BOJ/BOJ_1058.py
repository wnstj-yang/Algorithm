# Baekjoon Online Judge - 1058번. 친구

from collections import deque


def bfs(n):
    global ans
    visited = [False] * N
    visited[n] = True
    q = deque()
    q.append((n, 0))
    cnt = 0
    while q:
        x, y = q.popleft()
        # 2-친구는 2까지 카운트된 것이므로 2 이상이면 더이상 X
        if y >= 2:
            continue

        for i in range(N):
            # 친구의 친구라면 cnt증가
            if not visited[i] and friends[x][i] == 'Y':
                cnt += 1
                visited[i] = True
                q.append((i, y + 1))
    if ans < cnt:
        ans = cnt


N = int(input())
ans = 0
friends = [list(input()) for _ in range(N)]
# 순서대로 친구를 찾는ㄷ
for i in range(N):
    bfs(i)
print(ans)

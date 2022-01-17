# Baekjoon Online Judge - 2251번. 물통
# 참고함

from collections import deque


def check(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))


A, B, C = map(int, input().split())
visited = [[False] * (B + 1) for _ in range(A + 1)] # (x, y, z)로 리스트에 방문체크 대신 2차원 리스트사용(x, y) 동일함
ans = []
q = deque()
q.append((0, 0))
visited[0][0] = True
while q:
    x, y = q.popleft()
    z = C - x - y
    if x == 0:
        ans.append(z)
    # 총 6가지의 방법으로 물을 옮길 수 있다. A->B, A->C, B->A, B->C, C->A, C->B
    # 한 물통이 비거나 다른 한 물통이 가득 차야되므로 min함수를 사용한다
    water = min(x, B-y) # A -> B
    check(x-water, y+water)
    water = min(x, C-z) # A -> C
    check(x-water, y)
    water = min(y, A-x) # B -> A
    check(x+water, y-water)
    water = min(y, C-z) # B -> C
    check(x, y-water)
    water = min(z, A-x) # C -> A
    check(x+water, y)
    water = min(z, B-y) # C -> B
    check(x, y+water)

ans.sort()
print(*ans)

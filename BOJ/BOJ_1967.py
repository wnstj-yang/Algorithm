# Baekjoon Online Judge - 1967번. 트리의 지름

# 예제에만 휘둘리니 이진트리로 자꾸 생각하게되서 시간이 오래걸림
# 첫 번째 시도 : 이진트리라 생각하여 이에 대해 루트 노드 기준 왼쪽 오른쪽 더하는 방식 => 이진트리 조건에 없음
# 두 번째 시도 : 시간 초과 대비하여 visited를 방문한 리프노드는 안가는 방식으로 진행하였으나
# 여전히 시간초과 발생
from collections import deque


def search_max(start, end):
    global ans
    queue = deque()
    temp_visited[start] = 1
    queue.append((start, 0))
    while queue:
        x, result = queue.popleft()
        for i in range(len(child[x])):
            if child[x][i][0] == end:
                result += child[x][i][1]
                if result > ans:
                    ans = result
                return
            else:
                if temp_visited[child[x][i][0]] == 0:
                    temp_visited[child[x][i][0]] = 1
                    queue.append((child[x][i][0], result + child[x][i][1]))


n = int(input())
child = [[] for _ in range(n+1)]
weight = [[0] * 2 for _ in range(n+1)]
ans = 0
for i in range(n-1):
    x, y, z = map(int, input().split())
    child[x].append((y, z))
    child[y].append((x, z))

leaf = []
for i in range(1, len(child)):
    if len(child[i]) == 1:
        leaf.append(i)
# print(leaf)
#
# for i in child:
#     print(i)
visited = [0] * (n+1)
for i in range(len(leaf)-1):
    for j in range(i+1, len(leaf)):
        temp_visited = list(visited)
        search_max(leaf[i], leaf[j])
        visited[leaf[j]] = 1
    visited[leaf[i]] = 1

print(ans)

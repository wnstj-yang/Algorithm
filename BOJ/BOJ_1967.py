# Baekjoon Online Judge - 1967번. 트리의 지름

# 예제에만 휘둘리니 이진트리로 자꾸 생각하게되서 시간이 오래걸림
# 첫 번째 시도 : 이진트리라 생각하여 이에 대해 루트 노드 기준 왼쪽 오른쪽 더하는 방식 => 이진트리 조건에 없음
# 두 번째 시도 : 시간 초과 대비하여 visited를 방문한 리프노드는 안가는 방식으로 진행하였으나
# 여전히 시간초과 발생
# 세 번째 시도(참고함) : 1. root로부터 최대 값에 해당하는 인덱스를 구함 2. 해당 인덱스로부터 경로의 최대값을 구한 것이 최대 지름
from collections import deque


def search_max(start, mode):
    queue = deque()
    queue.append(start)
    # 방문 체크 시 -1로 초기화를 진행해야 visited안의 값으로 가중치를 더하는데 수월함
    visited = [-1 for _ in range(n+1)]
    visited[start] = 0
    while queue:
        x = queue.popleft()
        for i, weight in child[x]:
            if visited[i] == -1:
                # 방문하지 않았을 때 그 노드까지의 값을 가중치와 더해줘야한다.
                visited[i] = visited[x] + weight
                queue.append(i)
    # 최대 값을 가진 인덱스를 return
    if mode == 1:
        return visited.index(max(visited))
    else:
        return max(visited)


n = int(input())
child = [[] for _ in range(n+1)]
ans = 0
# 무방향
for i in range(n-1):
    x, y, z = map(int, input().split())
    child[x].append((y, z))
    child[y].append((x, z))

# 첫번째로 루트로부터 가장 최대값을 가진 인덱스를 구하고, 두번째로 그 인덱스로부터 시작해서 최대 값을 가진 것이 최대 지름임
print(search_max(search_max(1, 1), 2))

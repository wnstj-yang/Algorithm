# Baekjoon Online Judge - 1939번. 중량제한

from collections import deque


def bfs(mid):
    visited = [False] * (N + 1)
    visited[depart] = True
    q = deque()
    q.append(depart)
    while q:
        current = q.popleft()
        # 도착했다면 해당 무게값(mid)는 통과
        if current == arrive:
            return True

        for next, weight in islands[current]:
            # 방문하지 않았고 무게가 다리의 무게보다 작거나 같다면 경로인식
            if not visited[next] and mid <= weight:
                visited[next] = True
                q.append(next)
    return False


N, M = map(int, input().split())
islands = [[] for _ in range(N + 1)]
start = 1
end = int(1e9)
for _ in range(M):
    a, b, c = map(int, input().split())
    islands[a].append((b, c))
    islands[b].append((a, c))
depart, arrive = map(int, input().split()) # 출발, 도착지점
# 이분 탐색으로 최대인 값을 찾아나선다.
# 두 섬 연결할 때 하나의 다리가 있지 않기 때문에 다리들 중 최소값을 찾아서 하나의 다리로 지정하기에는 답이 안나온다.
# 그래서 이분 탐색으로 하나의 경로에서 각 다리를 지날 수 있는 최대 값을 찾아나선다.
while start <= end:
    mid = (start + end) // 2
    # 도착지까지 경로가 맞다하더라도 최대가 아닐 수 있기 때문에 mid값을 늘린다.
    if bfs(mid):
        start = mid + 1
    # 경로가 만들어지지 않는다면 값을 줄여나간다.
    else:
        end = mid - 1
print(end)

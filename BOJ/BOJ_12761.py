# Baekjoon Online Judge - 12761번. 돌다리

# 최단거리를 구하는 거여서 방문체크로 이미 방문했다면 그 것이 최단으로 도착한 것이므로 방문체크를 한다.
from collections import deque

# bfs로 구현
def bfs():
    queue = deque()
    queue.append(N)
    visited = [0] * 100001
    visited[N] = 1
    cnt = 0
    while queue:
        length = len(queue)
        for i in range(length):
            x = queue.popleft()
            for j in range(8):
                result = 0
                # 0, 1인덱스는 A, B배 만큼 이동하는 것이므로 곱하기 한다.
                if j <= 1:
                    result = x * num[j]
                # 그이외에는 더해준다( 음수는 리스트에 이미 저장했음(num))
                else:
                    result = x + num[j]
                # 범위 벗어남을 방지
                if result < 0 or result > 100000:
                    continue
                else:
                    if result == M:
                        return cnt + 1
                    elif visited[result] == 0:
                        queue.append(result)
                        visited[result] = 1
        # 한 바퀴를 큐의 길이로 정하고 이를 지났으면 cnt + 1
        cnt += 1


A, B, N, M = map(int, input().split())
num = [A, B, A, B, -A, -B, 1, -1]
print(bfs())

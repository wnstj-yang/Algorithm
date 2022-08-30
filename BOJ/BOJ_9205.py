# Baekjoon Online Judge - 9205번. 맥주 마시면서 걸어가기


from collections import deque


def bfs():
    q = deque()
    q.append([h_x, h_y])
    visited = [False] * N
    # 음수인 좌표값도 있기 때문에 절대값 적용
    while q:
        x, y = q.popleft()
        # 큐에 있는 좌표에서 페스티벌 좌표 거리가 1000이하라면 도착할 수 있다.
        if abs(x - f_x) + abs(y - f_y) <= 1000:
            print('happy')
            return
        for i in range(N):
            if not visited[i]:
                s_x, s_y = stores[i]
                # 각 편의점 좌표와 현재 좌표의 거리를 구하고 1000이하라면 해당 위치까지 갈 수 있어서 도착할 수 있는 후보로 큐에 넣음
                if abs(x - s_x) + abs(y - s_y) <= 1000:
                    q.append((s_x, s_y))
                    visited[i] = True
    print('sad')
    return


T = int(input())

for _ in range(T):
    N = int(input())
    h_x, h_y = map(int, input().split())
    stores = []
    for _ in range(N):
        x, y = map(int, input().split())
        stores.append((x, y))
    f_x, f_y = map(int, input().split())
    bfs()

# Baekjoon Online Judge - 11123번. 양 한마리... 양 두마리...


# x, y 바꿔서 해봤다.
T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(T):
    H, W = map(int, input().split())
    grid = []
    answer = 0
    for _ in range(H):
        info = list(input())
        grid.append(info)
    visited = [[False] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if not visited[y][x] and grid[y][x] == '#':
                answer += 1
                q = []
                q.append((y, x))
                visited[y][x] = True
                while q:
                    c, r = q.pop(0)
                    for i in range(4):
                        nr = r + dy[i]
                        nc = c + dx[i]
                        if nc < 0 or nc >= H or nr < 0 or nr >= W:
                            continue
                        if not visited[nc][nr] and grid[nc][nr] == '#':
                            q.append((nc, nr))
                            visited[nc][nr] = True
    print(answer)

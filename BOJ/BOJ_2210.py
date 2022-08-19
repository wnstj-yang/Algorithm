# Baekjoon Online Judge - 2210번. 숫자판 점프


def dfs(x, y, cnt, result):
    if cnt == 6:
        ans.add(tuple(result))
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        result.append(arr[nx][ny])
        dfs(nx, ny, cnt + 1, result)
        result.pop()


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = []
ans = set()
for _ in range(5):
    arr.append(list(map(str, input().split())))

for i in range(5):
    for j in range(5):
        dfs(i, j, 0, [])
print(len(ans))


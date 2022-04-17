# 110~111p 예제 - 상하좌우

N = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)]
direct_info = {
    'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]
}
directions = list(map(str, input().split()))
x, y = 1, 1
for direct in directions:
    nx = x + direct_info[direct][0]
    ny = y + direct_info[direct][1]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    else:
        x, y = nx, ny
print(x, y)


# 입력 - 1
# 5
# R R R U D D
# 출력 - 1
# 3 4

# Baekjoon Online Judge - 21608번. 상어 초등학교


N = int(input())
board = [[0] * N for _ in range(N)]
scores = {
    0: 0,
    1: 1,
    2: 10,
    3: 100,
    4: 1000
}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
students = {}
calculate_board = [[0] * N for _ in range(N)]
result = 0
for _ in range(N * N):
    info = list(map(int, input().split()))
    students[info[0]] = info[1:]

for key, val in students.items():
    candi = []
    stu_num = key
    like_list = val
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                like_cnt = 0
                empty_cnt = 0
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if board[nx][ny] in like_list:
                        like_cnt += 1
                    elif board[nx][ny] == 0:
                        empty_cnt += 1
                candi.append((like_cnt, empty_cnt, x, y))
    candi.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    x, y = candi[0][2], candi[0][3]
    board[x][y] = stu_num


for x in range(N):
    for y in range(N):
        like_list = students[board[x][y]]
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[nx][ny] in like_list:
                cnt += 1
        result += scores[cnt]
print(result)

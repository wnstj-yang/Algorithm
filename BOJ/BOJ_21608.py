# Baekjoon Online Judge - 21608번. 상어초등학교

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(x, y, numbers):
    cnt = 0
    f_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        else:
            if classroom[nx][ny] in numbers:
                f_cnt += 1
            if classroom[nx][ny] == 0:
                cnt += 1
    return cnt, f_cnt


N = int(input())
students = []
satisfy = {}
# 각 학생과 좋아하는 학생의 번호를 딕셔너리로 생성
for _ in range(N*N):
    temp = list(map(int, input().split()))
    students.append(temp)
    satisfy[temp[0]] = temp[1:]

# N^2의 격자판(학생들이 앉는 위치의 현황판느낌)
classroom = [[0] * N for _ in range(N)]
ans = 0
for student in students:
    spots = []
    f_spots = []
    max_val = 0
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                # 인접한 곳에서 친구들이 몇명인지 확인
                cnt, f_cnt = check(i, j, student[1:])
                if f_cnt != 0:
                    f_spots.append((f_cnt, cnt, i, j))
                else:
                    spots.append((f_cnt, cnt, i, j))

    # 같은게 여러개일 경우 인접한 곳에 비어있는 칸이 가장 많은 것 택
    selected = []
    max_cnt = 0
    max_idx = 0
    if f_spots:
        for s in f_spots:
            if len(selected) == 0:
                selected = s
            if s[0] > max_cnt:
                selected = s
                max_cnt = s[0]
            elif s[0] == max_cnt:
                if selected[1] < s[1]:
                    selected = s
                elif selected[1] == s[1]:
                    if selected[2] > s[2]:
                        selected = s
                        max_cnt = selected[2]
                    elif selected[2] == s[2]:
                        if selected[3] > s[3]:
                            selected = s
                            max_cnt = selected[3]
    else:
        for s in spots:
            if len(selected) == 0:
                selected = s
            if s[1] > max_cnt:
                selected = s
                max_cnt = s[1]
            elif s[1] == max_cnt:
                if selected[2] > s[2]:
                    selected = s
                    max_cnt = s[2]
                elif selected[2] == s[2]:
                    if selected[3] > s[3]:
                        selected = s
                        max_cnt = s[3]

    classroom[selected[2]][selected[3]] = student[0]

# 만족도 합 구하기
chart = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
for i in range(N):
    for j in range(N):
        temp, f_cnt = check(i, j, satisfy[classroom[i][j]])
        ans += chart[f_cnt]
print(ans)







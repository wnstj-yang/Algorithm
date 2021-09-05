# Baekjoon Online Judge - 21608번. 상어초등학교

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 인접한 곳을 체크한다
def check(x, y, numbers):
    # 인접한 곳에서 비어있는 곳 개수
    cnt = 0
    # 인접한 곳에서 좋아하는 친구의 수
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
# 각 학생과 좋아하는 학생의 번호를 딕셔너리로 생성
satisfy = {}
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
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                # 인접한 곳에서 친구들이 몇명인지 확인(비어 있는 곳도 같이 확인)
                cnt, f_cnt = check(i, j, student[1:])
                # 인접한 곳에 좋아하는 친구들이 없으면 spots에 저장, 아니면 f_spots(친구들 위치)에 저장
                if f_cnt != 0:
                    f_spots.append((f_cnt, cnt, i, j))
                else:
                    spots.append((f_cnt, cnt, i, j))

    # 같은게 여러개일 경우 인접한 곳에 비어있는 칸이 가장 많은 것 택
    selected = []
    max_cnt = 0
    max_idx = 0
    # 인접한 친구들이 있다면 거기에서 최대를 찾는다
    if f_spots:
        for s in f_spots:
            # 비어있다면 (첫 선택) 처음 거를 선택으로 넣어주고 진행
            if len(selected) == 0:
                selected = s
            # 인접한 친구들이 최대 수 보다 크다면 바꾼다
            if s[0] > max_cnt:
                selected = s
                max_cnt = s[0]
            # 같다면
            elif s[0] == max_cnt:
                # 비어있는 개수가 많은지 확인한다.
                if selected[1] < s[1]:
                    selected = s
                # 이 마저도 같다면 행이 작은 것을 넣고
                elif selected[1] == s[1]:
                    if selected[2] > s[2]:
                        selected = s
                        max_cnt = selected[2]
                    # 행도 같다면 열이 작은 것을 넣는다
                    elif selected[2] == s[2]:
                        if selected[3] > s[3]:
                            selected = s
                            max_cnt = selected[3]
    # 인접한 친구가 없다면 비어있는 수대로 비교
    else:
        for s in spots:
            # 초기 값 넣어줌
            if len(selected) == 0:
                selected = s
            # 비어있는 개수의 수가 최대 수 보다 크다면 넣어주고
            if s[1] > max_cnt:
                selected = s
                max_cnt = s[1]
            # 같다면
            elif s[1] == max_cnt:
                # 행의 수가 더 작은 거를 넣는다.
                if selected[2] > s[2]:
                    selected = s
                    max_cnt = s[2]
                # 그것마저도 같다면 열이 더 작은거를 넣는다
                elif selected[2] == s[2]:
                    if selected[3] > s[3]:
                        selected = s
                        max_cnt = s[3]
    # 각 위치에 해당하는 학생의 좌표를 따서 넣어준다
    classroom[selected[2]][selected[3]] = student[0]

# 만족도 합 구하기
chart = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
for i in range(N):
    for j in range(N):
        # 만족도를 위해 각 위치에있는 학생이 좋아하는 학생의 수를 계산한다
        temp, f_cnt = check(i, j, satisfy[classroom[i][j]])
        ans += chart[f_cnt]
print(ans)







# Baekjoon Online Judge - 3085. 사탕 게임
# 시간이 많이 쓰이는 듯 함


def row():
    global ans
    for i in range(N):
        # 행의 시작이니까 1로 초기화
        cnt = 1
        for j in range(N-1):
            # 인접한 것이 같다면 갯수 + 1
            if candies[i][j] == candies[i][j + 1]:
                cnt += 1
            # 다르다면 여태까지 카운트한 사탕의 개수를 정답과 비교
            else:
                if cnt > ans:
                    ans = cnt
                cnt = 1
        if cnt > ans:
            ans = cnt


# 위의 행의 아이디어처럼 열도 같다
def column():
    global ans
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if candies[j][i] == candies[j + 1][i]:
                cnt += 1
            else:
                if cnt > ans:
                    ans = cnt
                cnt = 1
        if cnt > ans:
            ans = cnt


N = int(input())
candies = [list(input()) for _ in range(N)]
ans = 0
# 가로로 인접한 것 바꾸기
for i in range(N):
    for j in range(N-1):
        candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
        row()
        column()
        candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]

# 세로로 인접한 것 바꾸기
for i in range(N):
    for j in range(N-1):
        candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]
        row()
        column()
        candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]
print(ans)

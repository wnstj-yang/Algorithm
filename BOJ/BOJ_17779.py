# Baekjoon Online Judge - 17779번. 게리맨더링 2

def check(x, y, d1, d2):
    global people
    temp = [[0] * (N+1) for _ in range(N+1)]
    each_area = [0] * 5
    temp[x][y] = 5
    # 조건에 따라 경계선을 구한다
    for i in range(1, d1+1):
        temp[x + i][y - i] = 5
    for i in range(1, d2+1):
        temp[x + i][y + i] = 5
    for i in range(1, d2+1):
        temp[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1+1):
        temp[x + d2 + i][y + d2 - i] = 5

    # 1번 선거구
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if temp[r][c] == 5:
                break
            else:
                each_area[0] += area[r][c]
    # 2번 선거구 => 열의 조건이 y < c <= N이므로 거꾸로 진행을 해서 경계 5까지의 값을 확인한다.
    for r in range(1, x+d2+1):
        for c in range(N, y, -1):
            if temp[r][c] == 5:
                break
            else:
                each_area[1] += area[r][c]
    # 3번 선거구
    for r in range(x+d1, N+1):
        for c in range(1, y-d1+d2):
            if temp[r][c] == 5:
                break
            else:
                each_area[2] += area[r][c]
    # 4번 선거구 => 열의 조건이 y-d1+d2 <= c <= N 이므로 거꾸로 진행을 해서 경계 5까지의 값을 확인한다.
    for r in range(x+d2+1, N+1):
        for c in range(N, y-d1+d2-1, -1):
            if temp[r][c] == 5:
                break
            else:
                each_area[3] += area[r][c]
    # 5번 선거구는 따로 안하고 area안의 총 인구수 합에서 1~4번 선거구 인구를 빼준다
    each_area[4] = people - sum(each_area)

    return max(each_area) - min(each_area)


N = int(input())
# 조건의 범위에 맞게 앞에 0을 추가한다.
area = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
answer = 987654321
people = 0
for each in area:
    people += sum(each)

for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if N < x + d1 + d2:
                    continue
                if y - d1 < 1 or N < y + d2:
                    continue

                num = check(x, y, d1, d2)
                if answer > num:
                    answer = num
print(answer)



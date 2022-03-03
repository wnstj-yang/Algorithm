# Baekjoon Online Judge - 2630번. 색종이 만들기

def count_color(n, x, y):
    global blue, white
    # 영역 내 다른 것이 있는지 판단
    wrong = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 다르다면 더이상 안 찾아본다.
            if area[x][y] != area[i][j]:
                wrong = True
                break
        if wrong:
            break
    # 다르지 않을 때 기준된느 값이 1이면 blue 추가, 0이면 white 추가
    if not wrong:
        if area[x][y]:
            blue += 1
        else:
            white += 1
    # 다르다면 더 분할 진행
    else:
        count_color(n // 2, x, y)
        count_color(n // 2, x, y + n // 2)
        count_color(n // 2, x + n // 2, y)
        count_color(n // 2, x + n // 2, y + n // 2)


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
blue, white = 0, 0
count_color(N, 0, 0)
print(white)
print(blue)

# 프로그래머스 - 바탕화면 정리

def solution(wallpaper):
    answer = []
    INF = 987654321
    # 왼쪽 위의 좌표는 가장 작은 값
    lux, luy, = INF, INF
    # 오른쪽 아래 좌표는 가장 큰 값
    rdx, rdy = 0, 0
    wallpaper = [list(item) for item in wallpaper]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
    answer = [lux, luy, rdx + 1, rdy + 1]
    return answer

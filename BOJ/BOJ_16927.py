# Baekjoon Online Judge - 16927번. 배열 돌리기 2

N, M, R = map(int, input().split())
# 회전 수에 나머지연산을 해서 돌린다. R(회전) 수가 크기 때문에 중복되는 회전이 존재하기 때문
arr = [list(map(int, input().split())) for _ in range(N)]
# 회전하려는 횟수
temp = min(N, M)

# 시작점이자 횟수에 따라 바깥에서부터 안으로 격자의 크기 시작점
x, y = 0, 0
while x < temp // 2 and y < temp // 2:
    # 각 격자의 가로길이 - 1 * 2 + 세로길이 - 1 * 2
    # checkpoint : 바깥쪽 격자만 나머지연산 후 같은 횟수만큼 돌면 안된다.
    # 각 격자당 갯수가 다르기 때문에 다른 결과가 나올 수 있음 !!!
    cnt = R % ((N - x - 1) * 2 + (M - y - 1) * 2)
    for _ in range(cnt):
        value = arr[x][y]
        # 상 -> 하
        for i in range(x+1, N):
            prev = arr[i][y]
            arr[i][y] = value
            value = prev
        # 좌 -> 우
        for j in range(y+1, M):
            prev = arr[N-1][j]
            arr[N-1][j] = value
            value = prev
        # 하 -> 상
        for i in range(N-2, x-1, -1):
            prev = arr[i][M-1]
            arr[i][M-1] = value
            value = prev
        # 우 -> 좌
        for j in range(M-2, y-1, -1):
            prev = arr[x][j]
            arr[x][j] = value
            value = prev
    # 바깥 -> 안 격자가 생기므로 좌표값 + 1을 하고,
    # N과 M은 기존 크기보다 1씩 줄어든다
    x += 1
    y += 1
    N -= 1
    M -= 1
for item in arr:
    print(*item)


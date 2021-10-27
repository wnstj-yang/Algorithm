# Baekjoon Online Judge - 17276번. 배열 돌리기

def rotate(dir):
    # deepcopy 대신 list slicing으로 복사하는 것이 더 빠르다
    temp = [item[:] for item in numbers]
    n = N - 1
    if dir:
        # 시계 방향일 때
        for i in range(N):
            # 1. 주 대각선을 가운데 열로 옮긴다.
            temp[i][N//2] = numbers[i][i]
            # 2. 가운데 열을 부 대각선으로 옮긴다.
            temp[i][n] = numbers[i][N//2]
            # 3. 부 대각선을 가운데 행으로 옮긴다.
            temp[N//2][n] = numbers[i][n]
            # 4. 가운데 행을 주 대각선으로 옮긴다.
            temp[n][n] = numbers[N//2][n]
            n -= 1
    # 반시계 방향일 때
    else:
        for i in range(N):
            # 1. 주 대각선을 가운데 행으로 옮긴다.
            temp[N//2][i] = numbers[i][i]
            # 2. 가운데 행을 부 대각선으로 옮긴다.
            temp[n][i] = numbers[N//2][i]
            # 3. 부 대각선을 가운데 열로 옮긴다.
            temp[n][N//2] = numbers[n][i]
            # 4. 가운데 열을 주 대각선으로 옮긴다.
            temp[n][n] = numbers[n][N//2]
            n -= 1
    return temp


T = int(input())
for _ in range(T):
    N, d = map(int, input().split())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    # 시계인지 반시계방향인지 판단
    dir = True
    if d < 0:
        dir = False
        d = abs(d)
    d = d // 45
    for _ in range(d):
        numbers = rotate(dir)
    for item in numbers:
        print(*item)

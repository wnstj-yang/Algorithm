# Baekjoon online Judge - 1074번. Z
import sys


def search(x, y, n):
    global cnt
    # 1. r, c를 찾으면 끝내기
    if x == r and y == c:
        print(cnt)
        sys.exit(0) # 프로그램 종료

    # 2. 못찾았으면 분할할 수 있는 최소부분을 명해야 recursionerror가 안나타남
    if n == 1:
        cnt += 1
        return

    # 3. (r, c)가 분할된 부분에 존재하지 않는 경우 그 크기만큼 이동했다고 가정하고 더해준다
    if not (x <= r < x + n and y <= c < y + n):
        cnt += n ** 2
        return

    # 4. 4분할
    search(x, y, n // 2)
    search(x, y + n // 2, n // 2)
    search(x + n // 2, y, n // 2)
    search(x + n // 2, y + n // 2, n // 2)


N, r, c = map(int, input().split())
cnt = 0
search(0, 0, 2 ** N)


# Baekjoon Online Judge - 10994번. 별 찍기 - 19


def add_stars(n, x, y):
    if n == 1:
        stars[x][y] = '*'
        return
    # 각 길이만큼 star를 채운다.
    length = 4 * n - 3
    for i in range(length):
        # 해당 길이만큼의 바깥부분들을 star로 채움
        stars[x][y + i] = '*'
        stars[x + i][y] = '*'
        stars[x + length - 1][y + i] = '*'
        stars[x + i][y + length - 1] = '*'
    # 그 다음 부분들을 채움 (n = 5, 4, 3....1)
    add_stars(n - 1, x + 2, y + 2)


N = int(input())
# 비어있는 부분들을 미리 초기화
stars = [[' '] * (4 * N - 3) for _ in range(4 * N - 3)]
add_stars(N, 0, 0)
for i in stars:
    print(''.join(i))

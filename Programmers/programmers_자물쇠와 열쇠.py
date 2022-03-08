# 90도씩 돌림
def rotate(arr, length):
    temp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            temp[j][length - 1 - i] = arr[i][j]
    return temp


def check(arr, N, M, r_key, lock):
    # 키를 움직이면서 자물쇠와 겹친 후 맞물리는 부분을 찾는다
    for i in range(N + M - 1):
        for j in range(N + M - 1):
            # 키에서 돌기 부분이면 전체 크기에 1을 더해준다
            # => 더해서 자물쇠가 모두 1이면 열리는 것임
            for x in range(M):
                for y in range(M):
                    if r_key[x][y] == 1:
                        arr[x + i][y + j] += 1
            # 정답인지 아닌지 판단 flag
            ans = True
            # 자물쇠에서 모두가 1인지 판단. 아니라면 열리지 않음
            for x in range(N):
                for y in range(N):
                    if arr[x + M - 1][y + M - 1] != 1:
                        ans = False
                        break
                if not ans:
                    break
            # 열리지 않으면 다시 값을 되돌린다.
            if not ans:
                for x in range(M):
                    for y in range(M):
                        if r_key[x][y] == 1:
                            arr[x + i][y + j] -= 1
            # 열리면 정답
            else:
                return True
    return False


def solution(key, lock):
    answer = True
    M = len(key)
    N = len(lock)
    # 자물쇠를 가운데로 놓고 범위를 늘리면서 키를 움직인다.
    # 그러기 위해서는 키의 길이 2배 + 자물쇠 길이 - 겹치는 부분 2를 진행한다.
    L = M * 2 + N - 2
    arr = [[0] * L for _ in range(L)]
    # 1. 0, 90, 180, 270회전한 key값들을 구한다
    key_90 = rotate(key, M)
    key_180 = rotate(key_90, M)
    key_270 = rotate(key_180, M)
    for i in range(N):
        for j in range(N):
            arr[i + M - 1][j + M - 1] = lock[i][j]
    # 각 0, 90, 180, 270도로 돌린 키 기준에서 맞물리는지 살펴본다
    if check(arr, N, M, key, lock):
        return True

    if check(arr, N, M, key_90, lock):
        return True

    if check(arr, N, M, key_180, lock):
        return True

    if check(arr, N, M, key_270, lock):
        return True

    return False

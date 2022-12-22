# Baekjoon Online Judge - 1592번. 영식이와 친구들


N, M, L = map(int, input().split())

arr = [0] * N
cnt = 0
idx = 0
while True:
    arr[idx] += 1
    if arr[idx] == M:
        print(cnt)
        break
    if arr[idx] % 2:
        idx = (idx + L) % N
    else:
        idx = (idx - L) % N
    cnt += 1

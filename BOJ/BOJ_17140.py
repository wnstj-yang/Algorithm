# Baekjoon Online Judge - 17140번. 이차원 배열과 연산


r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

time = 0
check = False
while time <= 100:
    N, M = len(arr), len(arr[0])
    if r < N and c < M:
        if arr[r][c] == k:
            check = True
            break
    if N >= M:
        for i in range(N):
            num_list = {}
            temp = []
            for j in range(M):
                num = arr[i][j]
                if num not in num_list:
                    num_list[num] = 1
                else:
                    num_list[num] += 1
            num_list = sorted(num_list.items(), key=lambda x: (x[1], x[0]))
            print(num_list)
            temp.extend(num_list)
            print(temp)
if check:
    print(time)
else:
    print(-1)
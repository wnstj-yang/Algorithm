# Baekjoon Online Judge - 17140번. 이차원 배열과 연산


def operation_R():
    max_M = 0
    for i in range(100):
        num_list = {}
        for j in range(100):
            num = arr[i][j]
            if num != 0:
                if num not in num_list:
                    num_list[num] = 1
                else:
                    num_list[num] += 1
        # 각 행에서의 수들을 정렬
        num_list = sorted(num_list.items(), key=lambda x: (x[1], x[0]))
        num_list = list(map(list, num_list))
        cnt = 0
        for x in range(len(num_list)):
            # [수, 나온 횟수]이기 때문에 2
            for y in range(2):
                arr[i][cnt] = num_list[x][y]
                cnt += 1
                # 첫 100개를 제외하기 때문에 갯수 카운트에서 100 이상인경우 X 
                if cnt >= 100:
                    break
            if cnt >= 100:
                break
        # R연산 시 열의 길이를 구한 후 나머지 부분은 0으로 채워준다
        max_M = max(max_M, cnt)
        for j in range(cnt, 100):
            arr[i][j] = 0
    return max_M


def operation_C():
    max_N = 0
    for j in range(100):
        num_list = {}
        for i in range(100):
            num = arr[i][j]
            if num != 0:
                if num not in num_list:
                    num_list[num] = 1
                else:
                    num_list[num] += 1
        num_list = sorted(num_list.items(), key=lambda x: (x[1], x[0]))
        num_list = list(map(list, num_list))

        cnt = 0
        for x in range(len(num_list)):
            for y in range(2):
                arr[cnt][j] = num_list[x][y]
                cnt += 1
                if cnt >= 100:
                    break
            if cnt >= 100:
                break
        max_N = max(max_N, cnt)
        for i in range(cnt, 100):
            arr[i][j] = 0
    return max_N


r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    info = list(map(int, input().split()))
    for j in range(3):
        arr[i][j] = info[j]

time = 0
N, M = 3, 3
check = False
while True:
    if arr[r][c] == k:
        check = True
        break

    if N >= M:
        M = operation_R()
    else:
        N = operation_C()
    time += 1
    if time > 100:
        break
if check:
    print(time)
else:
    print(-1)

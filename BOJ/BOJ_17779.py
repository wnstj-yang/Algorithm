# Baekjoon Online Judge - 17779번. 게리맨더링 2

def check(x, y, d1, d2):
    temp = [[0] + [0] * N for _ in range(N)]
    # 조건에 따라 경계선을 구한다
    for i in range(x, d1+1):
        temp[x + i][y - i] = 5


    return 1


N = int(input())
# 조건의 범위에 맞게 앞에 0을 추가한다.
area = [[0] + list(map(int, input().split())) for _ in range(N)]
answer = 987654321
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x >= x + d1 + d2:
                    continue
                if y - d1 >= y or y >= y + d2:
                    continue
                num = check(x, y, d1, d2)
                if ans > num:
                    ans = num
print(ans)



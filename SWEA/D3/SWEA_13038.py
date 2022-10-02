# SW Expert Academy - 13038번. 교환학생

# 그리디!! => 어느 요일에 시작하는 지에 따라 값이 다르기 때문에 체크해준다

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    days = list(map(int, input().split()))
    result = 987654321
    for i in range(7):
        if days[i]:
            idx = i
            cnt = 0
            temp_N = N
            while temp_N:
                if days[idx]:
                    temp_N -= 1
                cnt += 1
                idx = (idx + 1) % 7
            result = min(result, cnt)
    print('#{} {}'.format(tc, result))

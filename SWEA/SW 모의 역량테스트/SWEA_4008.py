# SW Expert Academy - 4008. [모의 SW 역량테스트] 숫자 만들기


def get_values(cnt, result):
    global max_val, min_val
    if cnt == N - 1:
        max_val = max(result, max_val)
        min_val = min(result, min_val)
        return

    for i in range(len(operators)):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:
                get_values(cnt + 1, result + numbers[cnt + 1])
            elif i == 1:
                get_values(cnt + 1, result - numbers[cnt + 1])
            elif i == 2:
                get_values(cnt + 1, result * numbers[cnt + 1])
            # 주의할점 : result // numbers[cnt + 1]은 내림으로 하고, int(result / numbers[cnt + 1])은 버림으로 처리한다.
            # -2 // 3이면 -1이 답이어야 하는데 -2가 나오기 때문.
            else:
                get_values(cnt + 1, int(result / numbers[cnt + 1]))
            operators[i] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_val = -987654321
    min_val = 987654321
    get_values(0, numbers[0])
    print('#{} {}'.format(tc, max_val - min_val))


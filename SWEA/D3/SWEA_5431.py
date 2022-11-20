# SW Expert Academy - 5431번. 민석이의 과제 체크하기

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = [False] * (N + 1)
    solved = list(map(int, input().split()))
    for num in solved:
        numbers[num] = True
    print('#{} '.format(tc), end='')
    answer = []
    for i in range(1, N + 1):
        if not numbers[i]:
            answer.append(i)
    print(*answer)

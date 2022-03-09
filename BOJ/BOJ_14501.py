# Baekjoon Online Judge - 14501번. 퇴사


def check(idx, result):
    global answer
    # 최대값 판단
    answer = max(result, answer)
    # 상담일 수를 벗어나는 경우
    if idx >= N + 1:
        return
    # 상담일 수가 가능한 경우와 하지 않으면 다음 날로
    if idx + numbers[idx][0] <= N + 1:
        check(idx + numbers[idx][0], result + numbers[idx][1])
        check(idx + 1, result)
    # 해당 범위가 넘어가게되면 다음날로 넘긴다.
    else:
        check(idx + 1, result)


N = int(input())
answer = 0
numbers = [(0, 0)]
for _ in range(N):
    a, b = map(int, input().split())
    numbers.append((a, b))

check(1, 0)
print(answer)

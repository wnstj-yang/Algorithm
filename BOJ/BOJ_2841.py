# Baekjoon Online Judge - 2841번. 외계인의 기타 연주

N, P = map(int, input().split())
stacks = [[] for _ in range(7)]
total = 0
for _ in range(N):
    n, p = map(int, input().split())
    # 각 번호의 스택에 값이 없는 경우 추가
    if not stacks[n]:
        stacks[n].append(p)
        total += 1
    else:
        # 있을 때 스택의 마지막 값이 p보다 크다면 가장 높은 프렛의 음을 발생 시킬 수 없으므로 손을 뗀다.
        while stacks[n] and stacks[n][-1] > p:
            stacks[n].pop()
            total += 1
        # 이후 stack에 값이 없으면 추가
        if not stacks[n]:
            stacks[n].append(p)
            total += 1
        else:
            # p보다 작으면 현재 p가 가장 높은 프렛의 음이므로 추가
            # 같은 경우는 따로 손을 떼지 않는다.
            if stacks[n][-1] < p:
                stacks[n].append(p)
                total += 1
print(total)

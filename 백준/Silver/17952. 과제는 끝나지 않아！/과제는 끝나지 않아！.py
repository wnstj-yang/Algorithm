N = int(input())
stack = []
result = 0
for _ in range(N):
    task = list(map(int, input().split()))
    # 과제가 주어졌을 때
    if task[0] == 1:
        score, time = task[1], task[2]
        time -= 1 # 과제 즉시 실행
        # 완료하면 점수 추가, 아니면 스택에 추가
        if time == 0:
            result += score
        else:
            stack.append([score, time])
    else:
        # 과제가 존재하는 경우에는 처리해준다
        if stack:
            score, time = stack[-1]
            time -= 1
            if time == 0:
                stack.pop()
                result += score
            # time부분에 1씩 감소
            else:
                stack[-1][1] -= 1
print(result)

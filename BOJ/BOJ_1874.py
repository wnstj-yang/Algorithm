# Baekjoon Online Judge - 1874번. 스택 수열

n = int(input())
stack = []
# 1 ~ n까지의 값을 idx로 정한다. (따로 list 설정 X => 시간 줄임)
idx = 1
ans = []
check = False
for i in range(n):
    target = int(input())
    while True:
        # 값이 n과 같거나 작은 상태의 조건과 target 값보다 작거나 같은 경우 push
        if idx <= n and idx <= target:
            stack.append(idx)
            idx += 1
            ans.append('+')
        # 스택에 있는 마지막 값이 target값과 같으면 pop => LIFO
        if stack[-1] == target:
            stack.pop()
            ans.append('-')
            break
        # n 범위를 넘어가거나 stack에 있는 값이 target보다 크면
        if idx > n + 1 or stack[-1] > target:
            check = True
            break
    if check:
        break
# 위의 check를 통해 표현되는 여부 판단
if check:
    print('NO')
else:
    for i in ans:
        print(i)


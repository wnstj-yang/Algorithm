# Baekjoon Online Judge - 14888번. 연산자 끼워넣기

def dfs(cnt, result):
    global max_num, min_num
    # cnt로 연산자의 개수 및 연산할 숫자 체크
    if cnt == N:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
    # 덧셈부터 넣음
    if oper[0] > 0:
        oper[0] -= 1
        dfs(cnt+1, result + numbers[cnt])
        oper[0] += 1
    # 뺄셈
    if oper[1] > 0:
        oper[1] -= 1
        dfs(cnt+1, result - numbers[cnt])
        oper[1] += 1
    # 곱셈
    if oper[2] > 0:
        oper[2] -= 1
        dfs(cnt+1, result * numbers[cnt])
        oper[2] += 1
    # 나눗셈
    if oper[3] > 0:
        oper[3] -= 1
        # 나눗셈의 경우 음수를 양수로 나눌 때 예외처리
        if result < 0:
            result = -result
            result = result // numbers[cnt]
            result = -result
        else:
            result = result // numbers[cnt]
        dfs(cnt+1, result)
        oper[3] += 1


N = int(input())
numbers = list(map(int, input().split()))
# 덧셈 - 뺄셈 - 곱셈 - 나눗셈
oper = list(map(int, input().split()))
max_num = -987654321
min_num = 987654321
dfs(1, numbers[0])
print(max_num)
print(min_num)

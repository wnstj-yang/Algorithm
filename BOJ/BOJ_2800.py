# Baekjoon Online Judge - 2800번. 괄호 제거

# 조합
def combi(n, cnt, idx):
    if cnt == n:
        result.append(list(temp))
        return
    # 조합을 구할 때 idx를 통해서 처음부터 탐색 X
    for i in range(idx, len(bracket_list)):
        if not visited[i]:
            visited[i] = True
            temp[cnt] = bracket_list[i]
            combi(n, cnt + 1, i)
            visited[i] = False


calculation = list(input())
# 괄호의 개수를 구한다
stack = []
bracket_list = []
answer = set()

# 괄호의 각각 위치에 대해서 공백으로 만들고, 괄호의 짝을 리스트로 저장
for i in range(len(calculation)):
    if calculation[i] == '(':
        stack.append(i)
        calculation[i] = ''
    elif calculation[i] == ')':
        calculation[i] = ''
        idx = stack.pop()
        bracket_list.append([idx, i])

for i in range(len(bracket_list)):
    temp = [0] * i
    result = []
    visited = [False] * len(bracket_list)
    combi(i, 0, 0)
    # 조합으로 구한, 즉 괄호의 짝들에 대해 조합으로 구한 결과들을 저장. (중복이 발생할 수 있으므로 집합 자료형 set 사용)
    for item in result:
        calul_copy = calculation[:]
        for x, y in item:
            calul_copy[x] = '('
            calul_copy[y] = ')'
        answer.add(''.join(calul_copy))
answer.add(''.join(calculation))

answer = sorted(answer)
for ans in answer:
    print(ans)


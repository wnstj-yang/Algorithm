def perm(n, length, visited, operators, ans):
    global seq
    if n == length:
        seq.append(list(ans))
        return
    for i in range(length):
        if not visited[i]:
            visited[i] = True
            ans[n] = operators[i]
            perm(n + 1, length, visited, operators, ans)
            visited[i] = False


def solution(expression):
    global seq
    answer = 0
    operators = []
    numbers = []
    idx = 0
    seq = []
    # 숫자와 연산자를 인덱스 슬라이싱으로 나누고 연산자 중복 방지
    for i in range(len(expression)):
        if expression[i] == '-' or expression[i] == '+' or expression[i] == '*':
            numbers.append(int(expression[idx:i]))
            numbers.append(expression[i])
            idx = i + 1
            if expression[i] not in operators:
                operators.append(expression[i])
    # 마지막 수 추가
    numbers.append(expression[idx:])
    ans = [0] * len(operators)  # 순열 순서
    visited = [False] * len(operators)  # 연산자 개수 및 방문 확인
    # 연산자 순열 구하기
    perm(0, len(operators), visited, operators, ans)
    # 순열로 구한 연산자 순서의 개수에 따라 반복문 시작
    for order in seq:
        result = 0
        temp = list(numbers)
        for o in order:
            i = 0
            while i < len(temp):
                value = 0
                if o == temp[i]:
                    if o == '-':
                        value = int(temp[i - 1]) - int(temp[i + 1])
                    elif o == '+':
                        value = int(temp[i - 1]) + int(temp[i + 1])
                    else:
                        value = int(temp[i - 1]) * int(temp[i + 1])
                    # integer는 iterable하지 않기 때문에 str형으로 list화
                    # list화 시 -100이면 split을 하지 않을 때 -, 1, 0, 0이므로
                    # split()을 통해 -100을 만들어준다
                    # 또한, String.split() 사용 시 리스트로 반환해준다
                    # 연산 값을 최신화
                    temp = temp[:i - 1] + list(str(value).split()) + temp[i + 2:]
                else:
                    i += 1

        answer = max(answer, abs(int(temp[0])))

    return answer
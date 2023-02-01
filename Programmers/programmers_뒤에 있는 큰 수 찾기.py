# 뒤에 있는 큰 수 찾기
# 스택을 활용해야함 ( 우선순위 큐 를 사용하는 사람도 있는 듯? )

def solution(numbers):
    answer = [0] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        # 스택에 있는 인덱스들을 통해 값을 비교해서 현재 보다 작다면 이전 것도 작아서 큰 수 적용이 될 수 있기 때문에
        # 큰 수가 됨
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    while stack:
        answer[stack.pop()] = -1
    return answer

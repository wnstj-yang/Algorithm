# 프로그래머스 - 택배상자

def solution(order):
    answer = 0
    stack = []
    idx = 0
    # stack처리를 해서 진행
    for i in range(1, len(order) + 1):
        stack.append(i)

        while stack:
            if stack[-1] == order[idx]:
                answer += 1
                idx += 1
                stack.pop()
            else:
                break

    return answer

def solution(x, n):
    answer = []
    idx = 1
    while idx <= n:
        answer.append(x * idx)
        idx += 1
    return answer
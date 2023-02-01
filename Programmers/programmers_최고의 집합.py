# 프로그래머스 - 최고의 집합

def solution(n, s):
    answer = []
    if n > s:
        return [-1]

    while n:
        num = s // n
        if num != 0:
            answer.append(num)
            s -= num
        else:
            answer.append(s % n)
            s = 0
        n -= 1
    return answer

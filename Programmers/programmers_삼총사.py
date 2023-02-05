# 삼총사

from itertools import combinations

def solution(number):
    answer = 0
    for item in combinations(number, 3):
        if sum(item) == 0:
            answer += 1
    return answer

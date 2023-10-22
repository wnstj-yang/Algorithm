import math

def solution(k, d):
    answer = 0
    # 원점으로부터 원의 방정식을 활용한다  x^2 + y^2 = d^2
    # 간격은 k / y = sqrt(d^2 - x^2)로 계산 / y값은 버림 처리
    for x in range(0, d + 1, k):
        y = math.floor(math.sqrt(d ** 2 - x ** 2)) # 여기 까지 하면 0 ~ y값 까지 고려하기 떄문에 y // k로 나눠야함
        answer += (y // k) + 1 # 1은 좌표 값 0도 고려한다
    return answer

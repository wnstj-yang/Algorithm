def solution(x):
    answer = True
    temp = x
    _sum = 0
    # x를 temp에 넣어 계산
    while temp != 0:
        # 각 자리수를 더해주고
        _sum += temp % 10
        # 10으로 나누어 계산이 끝난 자리수를 다시 초기화한다.
        temp = temp // 10
    # 나머지 연산으로 나누어떨어지지 않는다면 하샤드 수가 아님
    if x % _sum != 0:
        answer = False

    return answer
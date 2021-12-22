def solution(num):
    answer = 0
    while num != 1:
        # 500번이면 -1 반환
        if answer >= 500:
            answer = -1
            break
        # 짝수이면 2로 나눔
        if num % 2 == 0:
            num = num // 2
        # 홀수이면 3을 곱하고 + 1
        else:
            num = 3 * num + 1
        answer += 1 # 횟수 증가
    return answer
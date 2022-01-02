def solution(n):
    answer = ''
    # 3진법이므로 3의 나머지값과 몫으로 값을 계속 초기화 (0이 될 때까지)
    while n != 0:
        # 문자열형태로 3진법을 변화된 값을 뒤에다 더해주면 앞뒤반전이 진행된다.
        answer += str(n % 3)
        n //= 3 # 3으로 나눈 나머지를 n값으로
    return int(answer, 3)
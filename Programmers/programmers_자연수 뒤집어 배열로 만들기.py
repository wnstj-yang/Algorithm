def solution(n):
    answer = []
    # 1의 자리 숫자부터 넣는다
    while n > 0:
        answer.append(n % 10)
        n //= 10

    return answer
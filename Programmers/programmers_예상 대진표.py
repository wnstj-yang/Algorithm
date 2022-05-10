def solution(n,a,b):
    answer = 0
    # 문제대로 했을 시 시간초과 발생하므로
    # 다시 1번부터 N/2번까지 배정이라는 개념을 활용해서
    # 규칙을 찾음. 1을 더해서 2로 나눈다.(소수점은 버림)
    while True:
        if a == b:
            break
        else:
            a = (a + 1) // 2
            b = (b + 1) // 2
        answer += 1
    return answer

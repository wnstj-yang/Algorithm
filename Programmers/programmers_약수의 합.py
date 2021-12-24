def solution(n):
    answer = 0
    # 1 ~ n까지로 나누어서 떨어지면 약수
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer
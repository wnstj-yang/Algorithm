def solution(n):
    answer = 0
    sieve = [True] * (n+1) # 체(에라토스테네스의 체)
    # 제곱근까지의 연산만 해도 가능
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    for i in range(2, len(sieve)):
        if sieve[i]:
            answer += 1
    return answer
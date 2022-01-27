def solution(n):
    ans = 0
    # 거꾸로해서 2로 나머지 연산 했을 때 1이면 건전지 소모해야 하므로 기존 값에서 1을 빼준다
    # 나누어 떨어지면 기존 값을 2로 계속 나눈다
    while n != 0:
        if n % 2 == 1:
            n -= 1
            ans += 1
        else:
            n //= 2
    return ans
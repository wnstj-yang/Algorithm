def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]
    # 1 ~ 8은 숫자 N을 사용하는 횟수를 가리킨다.
    for i in range(1, 9):
        dp[i].add(int(str(N) * i)) # 숫자 N을 i만큼 표현할 수 있는 것
        for j in range(1, i):
            # i를 만들 수 있는 횟수들 사이의 사칙연산 진행
            # Ex) i = 4일 때 (1, 3), (3, 1) 횟수에서의 값들과 사칙연산
            for first in dp[j]:
                for second in dp[i - j]:
                    dp[i].add(first - second)
                    dp[i].add(first + second)
                    dp[i].add(first * second)
                    if second:
                        dp[i].add(first // second)
        if number in dp[i]:
            return i
    return -1

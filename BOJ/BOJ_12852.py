# Baekjoon Online Judge - 12852번. 1로 만들기 2

X = int(input())

dp = [0] * (X + 1)
numbers = [i for i in range(X + 1)]
numbers[1] = 0 # 들어갈 인덱스 0으로 초기화
for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1
    numbers[i] = i - 1
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        numbers[i] = i // 2
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        numbers[i] = i // 3
# numbers는 안에 만들어진 숫자들이 들어가 있으며 이는 인덱스 처리도 가능하다.
# 예를 들어 10이면 첫 10은 출력해주되 numbers[10] = 9, numbers[9] = 3, numbers[3] = 1, numbers[1] = 0 이므로
# 각 10 9 3 1 처럼 출력이 되는 것이다.
print(dp[X])
print(X, end=' ')
idx = X
while numbers[idx] != 0:
    print(numbers[idx], end=' ')
    idx = numbers[idx]

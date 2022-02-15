# Baekjoon Online Judge - 2631번. 줄세우기

# 가장 긴 증가하는 부분 수열의 수가 고정된 이후의 다른 아이들이 움직이기 때문에
# 답은 총 길이 - 가장 긴 증가하는 부분 수열의 수 이다. 
# 예시에서 3 7 5 2 6 1 4 에서 가장 긴 증가하는 부분 수열의 수는 3 5 6이며, 이는 고정되고 나머지 4개의 수가 움직임
N = int(input())
numbers = []
dp = [1] * N # 가장 긴 증가하는 부분 수열 구할 때 자기 자신은 포함
for _ in range(N):
    numbers.append(int(input()))

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))

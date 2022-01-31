# Baekjoon Online Judge - 11053번. 가장 긴 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N # 자기 자신을 포함한다는 의미에서 개수 1로 초기화

for i in range(N):
    # i번째까지 자기 포함된 dp에서의 가장 긴 증가하는 부분 수열의 개수 를 확인
    for j in range(i):
        if A[i] > A[j]: # i번째 까지의 부분 수열 중 i번째(현재) 수 보다 작으면 비교 
            dp[i] = max(dp[i], dp[j] + 1) # + 1은 자기 자신 포함된 것
print(max(dp))

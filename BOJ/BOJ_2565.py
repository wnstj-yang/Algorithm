# Baekjoon Online Judge - 2565번. 전깃줄

N = int(input())

# 최장 증가 부분수열 ( 몇 개를 제거해 교차하지 않는 전깃줄 최소 개수 )
lines = []
dp = [1] * N # 자기 자신
for _ in range(N):
    line = list(map(int, input().split()))
    lines.append(line)

lines.sort() # A 전봇대 기준 정렬
for i in range(N):
    for j in range(i):
        if lines[i][1] > lines[j][1]: # 겹치는 경우 A 전봇대 값보다 B 전봇대 값이 큰 경우 교차된다.
            dp[i] = max(dp[i], dp[j] + 1) # 이전의 경우까지 겹치지 않는 선들을 저장
print(N - max(dp)) # 총 연결된 수 - 이전까지 겹치지 않는 선들의 최대 개수 = 겹치는 최소 개수

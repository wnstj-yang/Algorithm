# 다이내믹 프로그래밍 - 226p 효율적인 화폐 구성

N, M = map(int, input().split())

prices = [] # 화폐 단위들

for _ in range(N):
    prices.append(int(input()))

dp = [10001] * (M + 1) # 화폐 가치의 크기가 최대인 것을 넣음
dp[0] = 0 # 0은 값이 없고 계산에 필요한 값
for i in range(N):
    # 주어진 화폐 단위의 처음부터 시작해서 M원까지 해당 화폐를(인덱스) 만들기 위한
    # 최소의 개수를 구한다.
    # 즉, dp리스트에는 화폐(인덱스)를 구하기 위해 최소 값(각 인덱스의 값)이 저장되어 있다.
    for j in range(prices[i], M + 1):
        dp[j] = min(dp[j], dp[j - prices[i]] + 1)
# 계산이 끝난 이후 값이 그대로 10001이면 구할 수 없으므로 -1을 출력
if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
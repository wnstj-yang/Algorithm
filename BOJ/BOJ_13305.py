# Baekjoon Online Judge - 13305번. 주유소

N = int(input())
dist = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_cost = 0
price = prices[0]
# 현재 도시의 값이 최소 값(이전 도시들 중에서의 최소)보다 작으면 현재 거리까지의 값으로 곱해서 더해주고, 
# 최소 값을 초기화 해주면서 값을 구해나간다.
# 예시에서 5 -> 2로갈 때 5가 초기 최소값이지만 2가 더 작으므로 5 * 2(거리)를 더해주고, 최소값은 2로 바꾼다.
# 이후에 4를 만나지만 2가 더 최소이므로 2 * 3(거리)를 또 더해준다
for i in range(1, N):
    min_cost += price * dist[i - 1]
    if price > prices[i]:
        price = prices[i]
print(min_cost)

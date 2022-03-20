# Baekjoon Online Judge - 11047번. 동전 0

N, K = map(int, input().split())
prices = []
result = 0
for _ in range(N):
    prices.append(int(input()))

for i in range(len(prices) - 1, -1, -1):
    price = prices[i]
    if K >= price:
        result += (K // price)
        K %= price
print(result)

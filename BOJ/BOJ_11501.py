# Baekjoon Online Judge - 11501번. 주식

T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    result = 0
    max_price = 0
    # 그리디적으로 앞에서부터가 아니라 끝에서부터 시작해서 가장 큰 값을 구하면서 현재 값이 가장 큰 값보다 작다면 이익이 난 것으로 더해나감
    for i in range(len(prices) - 1, -1, -1):
        max_price = max(max_price, prices[i])
        if prices[i] < max_price:
            result += max_price - prices[i]
    print(result)

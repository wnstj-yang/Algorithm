# SW Expert Academy - 1859번. 백만 장자 프로젝트

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    max_price = 0
    result = 0
    for i in range(len(prices) - 1, -1, -1):
        max_price = max(max_price, prices[i])
        if prices[i] < max_price:
            result += max_price - prices[i]
    print('#{} {}'.format(tc, result))
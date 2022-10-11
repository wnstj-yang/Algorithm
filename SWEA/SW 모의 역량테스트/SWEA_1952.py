# SW Expert Academy - 1952. [모의 SW 역량테스트] 수영장


def check_money(n, price):
    global result
    if n >= 12:
        result = min(result, price)
        return
    # 각 1일, 1달, 3달로 가격 계산진행
    check_money(n + 1, price + prices[0] * plan[n])
    check_money(n + 1, price + prices[1])
    check_money(n + 3, price + prices[2])


T = int(input())
for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    result = prices[3] # 1년 가격으로 놓고 가격들 체크
    check_money(0, 0)
    print('#{} {}'.format(tc, result))

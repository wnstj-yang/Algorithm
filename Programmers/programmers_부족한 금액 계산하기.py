def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        # 횟수만큼 price 증가
        answer += (price * i)
    # 부족한 금액 판단
    result = answer - money
    # 부족하지 않으면 0으로
    if result < 0:
        result = 0
    return result
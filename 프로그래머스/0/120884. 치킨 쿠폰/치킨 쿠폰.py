def solution(chicken):
    answer, total_coupon = 0, 0
    while chicken:
        service_chicken = chicken // 10
        left_coupon = chicken % 10
        total_coupon += chicken % 10
        answer += service_chicken
        chicken = service_chicken
    while total_coupon >= 10:
        new_chicken = total_coupon // 10
        total_coupon = total_coupon % 10 + new_chicken
        answer += new_chicken
    return answer

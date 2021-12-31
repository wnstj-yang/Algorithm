def solution(a, b):
    answer = 0
    x, y = 0, 0
    if a > b:
        x, y = b, a
    else:
        x, y = a, b
    # 혹은 min(a,b) ~ max(a, b)
    for i in range(x, y + 1):
        answer += i
    return answer
def solution(array, n):
    answer = 101
    min_val = 101
    for num in array:
        if min_val > abs(n - num):
            answer = num
            min_val = abs(n - num)
        elif min_val == abs(n - num):
            answer = min(answer, num)
    return answer
def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        for str_num in str(num):
            if str_num == str(k):
                answer += 1
    return answer
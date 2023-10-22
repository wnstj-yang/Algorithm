def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:(x[col - 1], -x[0]))
    for i in range(row_begin, row_end + 1):
        total = 0
        # 동일한 data원소 길이를 가지지 않을 수 있다. 그래서 인덱스로 직접 접근 지양
        for j in data[i - 1]:
            total += j % i
        answer ^= total

    return answer


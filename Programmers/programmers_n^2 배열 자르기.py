def solution(n, left, right):
    answer = []
    # 행, 열을 나머지와 몫으로 구분함
    # answer에 넣을 값은 행, 열의 수에 따라 저장
    while left <= right:
        row = left // n  # 행
        col = left % n  # 열
        # 열이 행보다 작으면 행의 수 + 1을 넣어준다
        if col < row:
            val = row + 1
        # 열이 행보다 크거나 같으면 열의 수 + 1을 넣어준다
        else:
            val = col + 1
        answer.append(val)
        left += 1

    return answer
def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0
    # 사실 상 가로 혹은 세로의 구분 없이 명함의 w, h 중 큰 값과 작은 값들의 최대 값을 구한다.
    # 예시에 있는 명함들의 가로 세로 길이들을 가로에는 [w, h] 중 큰 값을, 세로에는 작은 값을 구하고
    # 그 중에서 최대 값들을 구한 후 곱합니다.
    # Ex) [[60, 50], [30, 70], [60, 30], [80, 40]] 이면,
    # 가로 : [60, 70, 60, 80], 세로 : [50, 30, 30, 40]
    # 이 중 각 최대값은 가로 80, 세로 50이다.
    for size in sizes:
        max_num1, max_num2 = max(size), min(size)
        max_width = max(max_num1, max_width)
        max_height = max(max_num2, max_height)
    answer = max_width * max_height
    return answer

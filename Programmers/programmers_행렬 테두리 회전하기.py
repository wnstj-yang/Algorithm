def solution(rows, columns, queries):
    answer = []
    arr = [[0] * (columns + 1) for _ in range(rows + 1)]
    num = 1
    # 값 초기화
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr[i][j] = num
            num += 1

    for info in queries:
        x1, y1, x2, y2 = info[0], info[1], info[2], info[3]
        # 좌 -> 우
        value = arr[x1][y1]
        min_val = value
        for j in range(y1 + 1, y2 + 1):
            temp = arr[x1][j]
            arr[x1][j] = value
            value = temp
            min_val = min(min_val, value)
        # 상 -> 하
        for i in range(x1 + 1, x2 + 1):
            temp = arr[i][y2]
            arr[i][y2] = value
            value = temp
            min_val = min(min_val, value)
        # 우 -> 좌
        for j in range(y2 - 1, y1 - 1, -1):
            temp = arr[x2][j]
            arr[x2][j] = value
            value = temp
            min_val = min(min_val, value)
        # 하 -> 상
        for i in range(x2 - 1, x1 - 1, -1):
            temp = arr[i][y1]
            arr[i][y1] = value
            value = temp
            min_val = min(min_val, value)

        answer.append(min_val)
    return answer
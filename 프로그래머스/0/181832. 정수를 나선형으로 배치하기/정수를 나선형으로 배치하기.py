def solution(n):
    answer = [[0] * n for _ in range(n)]
    num = 1
    x, y = 0, 0
    while num <= n * n:
        # 1. 오른쪽으로 이동
        while y < n:
            # print('1', x, y)
            if answer[x][y] != 0:
                break
            answer[x][y] = num
            y += 1
            num += 1
        y -= 1
        x += 1
        # 2. 아래로 이동
        while x < n:
            # print('2', x, y)
            if answer[x][y] != 0:
                break
            answer[x][y] = num
            x += 1
            num += 1
        x -= 1
        y -= 1
        # 3. 왼쪽으로 이동
        while y >= 0:
            # print('3', x, y)
            if answer[x][y] != 0:
                break
            answer[x][y] = num
            y -= 1
            num += 1
        x -= 1
        y += 1
        # 4. 위쪽으로 이동
        while x >= 0:
            # print('4', x, y)
            if answer[x][y] != 0:
                break
            answer[x][y] = num
            x -= 1
            num += 1
        x += 1
        y += 1
        
    # for z in answer:
    #     print(z)
    return answer
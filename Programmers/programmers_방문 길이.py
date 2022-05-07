def solution(dirs):
    answer = 0
    x, y = 0, 0
    dist = []

    direction = {
        'U': [0, 1], 'D': [0, -1],
        'R': [1, 0], 'L': [-1, 0]
    }

    for d in dirs:
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 해당 경로를 사용했는지 안했는지 판별해야되기 때문에,
            # 가는 것과 오는 것 둘 다 처리해야 하는 것이 포인트였음
            if (x, y, nx, ny) not in dist:
                dist.append((x, y, nx, ny))
                dist.append((nx, ny, x, y))
            x, y = nx, ny
    answer = len(dist) // 2 # 좌표의 길이는 그러면 2배가 되므로 2로 나눈다
    return answer

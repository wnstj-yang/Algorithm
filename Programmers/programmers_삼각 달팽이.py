def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n + 1)] # 2차원 리스트로 진행(x, y좌표값)
    x, y = -1, 0 # 0, 0으로 초기화하면 x값에서 마지막에 인덱스를 벗어난다
    # Ex) n이 4일 때 인덱스상으로 x가 3까지 가야되는데 x를 4로 연산이 된 후 다음이 진행되서 인덱스 에러
    num = 1
    # 0: 아래 / 1: 오른쪽 / 2: 위
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            arr[x][y] = num
            num += 1
    # 2차원 리스트로 된것을 1차원으로 만들어준다
    for item in arr:
        answer.extend(item)

    return answer
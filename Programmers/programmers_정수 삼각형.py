def solution(triangle):
    answer = triangle[0][0] # 삼각형 꼭대기 값을 최댓값으로 지정
    # 각 삼각형의 높이를 기준으로 행마다 살펴본다
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            now = triangle[i][j] # 현재 값
            # 1. 첫 번째 값인 경우 그 위의 값과 더해서 넣는다
            if j == 0:
                triangle[i][j] = now + triangle[i - 1][0]
            # 2. 마지막 값인 경우도 그 위의 값과 더해서 넣는다
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = now + triangle[i - 1][j - 1]
            # 3. 그 이외의 경우 현재 값에서 대각선 왼쪽 위와 오른쪽 위와 더했을 때 최댓값을 넣는다
            else:
                triangle[i][j] = max(now + triangle[i - 1][j - 1], now + triangle[i - 1][j])
        # 4. 각 행마다 최댓값을 갱신했으므로 그 중에서 최댓값을 똑같이 갱신시킨다.
        answer = max(answer, max(triangle[i]))

    return answer

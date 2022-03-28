def solution(routes):
    answer = 0
    visited = [False] * len(routes)
    routes.sort(key=lambda x: x[1])  # 진출 지점 기준으로 정렬
    for i in range(len(routes)):
        # 진출 지점을 기준으로 각 경로들에 있어서 방문했는지에 따라 카메라 설치 유무 판단
        value = routes[i][1]
        if not visited[i]:
            visited[i] = True
            answer += 1  # 해당 카메라 설치
            # 현재 차량 진출 지점을 기준으로 방문안한 차량의 진입과 진출 사이에 값이 있으면 방문 표시
            # 즉, 카메라 하나로 커버되는 차량들이 존재하면 이후에 탐색할 필요없이 방문체크로 끝
            for j in range(len(routes)):
                if not visited[j] and routes[j][0] <= value <= routes[j][1]:
                    visited[j] = True

    return answer

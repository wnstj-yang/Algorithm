def solution(n, computers):
    answer = 0
    network = [[] * (n+1) for _ in range(n+1)]
    visited = [0] * (n+1)
    # 양방향 네트워크를 트리형태로 부모 자식간의 관계로 만든다.
    for i in range(n):
        for j in range(n):
            # 간선 연결 및 자기사진이 아니고 양방향일 때 중복이 들어가는 부분 방지
            if computers[i][j] == 1 and i != j and j+1 not in network[i+1]:
                network[i+1].append(j+1)
                network[j+1].append(i+1)
    # 노드를 하나씩 방문하면서 dfs해서 하나의 네트워크가 생성(경로) 살펴본다
    # 간선의 개수가 네트워크 개수를 의미하는 것은 아니다
    for i in range(1, n+1):
        if visited[i] == 0:
            stack = [i]
            while stack:
                num = stack.pop()
                visited[num] = 1
                for i in network[num]:
                    if visited[i] == 0:
                        stack.append(i)
            answer += 1
    return answer
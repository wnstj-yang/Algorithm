# SW Expert Academy - 6057번. 그래프의 삼각형


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    answer = 0
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    # 1 ~ N 정점을 각각 그래프안에 있는지, 사이클 형성 확인 => 삼각형
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            for k in range(j + 1, N + 1):
                if i in graph[j] and j in graph[k] and k in graph[i]:
                    answer += 1
    print('#{} {}'.format(tc, answer))

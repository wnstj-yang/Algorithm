# 그래프 이론 - 유형별. 어두운 길 397p
# 크루스칼


def find_parents(parents, x):
    if parents[x] != x:
        return find_parents(parents, parents[x])
    return parents[x]


def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())
parents = list(range(N))
edges = []
result = 0 # 전체 비용
min_cost = 0 # 모든 집들을 연결하는 최소 비용
for _ in range(M):
    a, b, cost = map(int, input().split())
    result += cost # 전체 비용 더해주기
    edges.append((cost, a, b))  # 비용을 기준으로 노드 저장

edges.sort() # 비용이 낮은 것부터 진행하기 위해 오름차순 정렬 진행
for edge in edges:
    cost, a, b = edge
    # 사이클이 생기지 않도록 같은 루트 노드인지 확인하는 작업이 필요하다
    if find_parents(parents, a) != find_parents(parents, b):
        min_cost += cost
        union_parents(parents, a, b)
print(result - min_cost)

# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

# 51
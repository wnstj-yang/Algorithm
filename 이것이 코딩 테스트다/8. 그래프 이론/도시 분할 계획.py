# 그래프 이론 - 도시 분할 계획. 300p
# 크루스칼 알고리즘

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합집합을 할 때 루트 노드 값이 작은 것에 값을 넣는다
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = list(range(N + 1))
edges = []
result = 0
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()
last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost # 간선들 중 마지막이 아니기 때문에 마지막 값을 갱신시켜줌
print(result - last)

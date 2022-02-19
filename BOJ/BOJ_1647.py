# Baekjoon Online Judge - 1647번. 도시 분할 계획
# 최소 신장 트리 => 모든 노드를 연결하되 사이클 존재 X

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
edges = []
result, last = 0, 0
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
for edge in edges:
    c, a, b = edge
    # 마지막 연결되는 부분을 구해서 모든 간선을 돌은 후 빼준다.
    # 그러면 분리되는 두 마을이 구해짐
    if find(a) != find(b):
        result += c
        last = c
        union(a, b)
print(result - last)

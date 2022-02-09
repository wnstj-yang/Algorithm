# Baekjoon Online Judge - 1197번. 최소 스패닝 트리

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
edge_list = []
result = 0
for _ in range(E):
    A, B, C = map(int, input().split())
    edge_list.append((C, A, B))
edge_list.sort() # 가중치 기준으로 오름차순 정렬

for edge in edge_list:
    C, A, B = edge
    if find(A) != find(B):
        union(A, B)
        result += C # 가중치 더한다
print(result)

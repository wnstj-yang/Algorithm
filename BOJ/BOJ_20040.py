# Baekjoon Online Judge - 20040번. 사이클 게임

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = list(range(N))
result = 0
for i in range(M):
    x, y = map(int, input().split())
    if find_parent(x) == find_parent(y):
        result = i + 1
        break
    else:
        union(x, y)
print(result)

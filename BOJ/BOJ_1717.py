# Baekjoon Online Judge - 1717번. 집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # 재귀 최대 깊이를 설정해야 통과됨


# 경로 압축 -> 부모 노드에 루트 노드를 입력
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    c, a, b = map(int, input().split())
    if c:
        if find(parent, a) == find(parent, b):
            print('YES')
        else:
            print('NO')
    else:
        union(parent, a, b)

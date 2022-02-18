# Baekjoon Online Judge - 1922번. 네트워크 연결


# 특정 원소가 속한 집합 찾기
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


# 두 원소가 속한 집합 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N = int(input())
M = int(input())
result = 0
computers = []
parents = [i for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    computers.append((c, a, b))
computers.sort() # 가중치 기준 오름차순으로 정렬

for computer in computers:
    c, a, b = computer
    # 사이클 방지
    if find(a) != find(b):
        result += c
        union(a, b)
print(result)

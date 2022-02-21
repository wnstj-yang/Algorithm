# Baekjoon Online Judge - 1976번. 여행 가자


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


N = int(input())
M = int(input())

parents = [i for i in range(N + 1)]
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    # 각 노드별 연결된 상태 파악(1이면 연결)
    for j in range(1, len(info) + 1):
        if info[j - 1]:
            union(i, j)
plan = list(map(int, input().split()))
result = 0
flag = True

for i in plan:
    val = parents[i]
    # 처음 루트 노드 값 설정
    if result == 0:
        result = val
        continue
    # 각 노드의 루트노드가 다르면 연결되지 않음을 의미한다.
    if val != result:
        flag = False

if flag:
    print("YES")
else:
    print("NO")


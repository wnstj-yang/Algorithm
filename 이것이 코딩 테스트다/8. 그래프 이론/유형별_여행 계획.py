# 그래프 이론 - 유형별. 여행 계획 393p

# 같은 집합안에 속하는 지 파악

# 부모 노드 찾는 함수
def find_parent(parents, x):
    if parents[x] != x:
        return find_parent(parents, parents[x])
    return parents[x]


# 하나의 집합을 합친다
def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
parents = list(range(N + 1))
orders = list(map(int, input().split()))
# 양방향 연결을 의미하고 연결된 상태라면 하나의 집합으로 인식하여 합친다
for i in range(N):
    for j in range(N):
        if board[i][j] == board[j][i] and board[i][j] == 1:
            union_parent(parents, i + 1, j + 1)

result = "YES" # 초기 값을 YES로 넣음
root_node = find_parent(parents, orders[0]) # 순서대로 돌 때 첫 번째를 기준으로 루트 노드를 구한다
# 그 다음으로 순서대로 부모 노드를 찾아서 루트 노드와 같은지 확인
# (편의 상 루트 노드와 부모 노드랑 분리하여 표현하였지만 동일)
for node in orders[1:]:
    if root_node != find_parent(parents, node):
        result = 'NO'
        break

print(result)


# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
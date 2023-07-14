# 그래프 이론 - 유형별. 탑승구 395p
# 풀이 보고 이해함
# 서로소 집합 개념 이용

# 루트 노트를 찾는다
def find_parent(parents, x):
    if parents[x] != x:
        return find_parent(parents, parents[x])
    return parents[x]


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


G = int(input()) # 탑승구 수
P = int(input()) # 비행기 수
cnt = 0
parents = list(range(G + 1)) # 탑승구들이 집합으로 각 연결 상태를 나타낸다
for _ in range(P):
    go_to_G = int(input())
    root_node = find_parent(parents, go_to_G)
    if root_node == 0:
        break
    # 입력의 의미는 1번부터 go_to_G까지 탑승구 번호까지 하나에 도킹할 수 있다는 의미이다.
    # 즉, go_to_G가 최대인 것이고, 비행기를 최대로 많이 도킹해야 하므로 채워나간다는 의미로
    # go_to_G에 비행기를 넣는다.
    # root_node에 1을 뺀 이유는 추후 다른 비행기가 같은 탑승구로 오더라도 그 이전으로
    # 넘겨서 도킹할 수 있게 차례대로 넣어줄 수 있기 때문이다.
    # 예를 들어 4번 탑승구로 들어갈 수 있으면 3번 탑승구와 union으로 집합 상태를 이룬다
    # 그러다가 0번까지(1번 탑승구까지 도킹이 완료될 시) 오게 되면 멈춘다.
    union_parent(parents, root_node - 1, root_node)
    cnt += 1
print(cnt)


# 4
# 3
# 4
# 1
# 1

# 2


# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4


# 3

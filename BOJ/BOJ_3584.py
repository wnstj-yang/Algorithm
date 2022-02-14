# Baekjoon Online Judge - 3584번. 가장 가까운 공통 조상

T = int(input())

for _ in range(T):
    N = int(input())
    tree = [0] * (N + 1)
    # 각 노드에 부모 노드 입력
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[b] = a
    x, y = map(int, input().split())
    # 자기 자신까지 포함이기 때문에 공통 조상을 찾기 위해 두 리스트에 값을 넣는다
    first = [x]
    second = [y]
    # 루트 노드까지 찾아나선다
    while tree[x] != 0:
        first.append(tree[x])
        x = tree[x]

    while tree[y] != 0:
        second.append(tree[y])
        y = tree[y]
    # 뒤에서부터 길이만큼 인덱스를 설정
    f_idx = len(first) - 1
    s_idx = len(second) - 1
    # 같지 않을 때 까지 찾고 마지막에 인덱스 + 1 해주어야 최소 공통 조상을 찾음
    while first[f_idx] == second[s_idx]:
        f_idx -= 1
        s_idx -= 1
    print(first[f_idx + 1])

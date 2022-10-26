# Baekjoon Online Judge - 1043번. 거짓말

def find_parent(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    # 지민이가 거짓말인 줄 아는 번호의 루트가 존재한다면 바꿔준다. 즉, 거짓말인 줄 아는 번호들을 루트 번호로 생각
    if parent_a in know_truth:
        parents[parent_b] = parent_a
    elif parent_b in know_truth:
        parents[parent_a] = parent_b
    else:
        if parent_a < parent_b:
            parents[parent_b] = parent_a
        else:
            parents[parent_a] = parent_b


N, M = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]
parents = list(range(N + 1))
parties = []
result = 0
for _ in range(M):
    info = list(map(int, input().split()))
    if info[0] == 1:
        parties.append([info[1]])
    else:
        party = info[1:]
        # 각 파티에 2명 이상인 경우 같은 풀에 있으므로 union(합)을 해준다
        for i in range(len(party) - 1):
            union(party[i], party[i + 1])
        parties.append(party)

for party in parties:
    is_known = False
    for num in party:
        if find_parent(parents[num]) in know_truth:
            is_known = True
            break
    if not is_known:
        result += 1
print(result)







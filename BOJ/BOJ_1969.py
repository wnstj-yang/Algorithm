# Baekjoon Online Judge - 1969번. DNA

N, M = map(int, input().split())
DNA_list = []
for _ in range(N):
    DNA_list.append(input())
ans = ''
h_dis = 0
# 해밍거리가 각 DNA간 비교인 것 같았으나
# 각 위치에 대한 것들을 비교한다
for i in range(M):
    A, T, G, C = 0, 0, 0, 0
    for j in range(N):
        if DNA_list[j][i] == 'A':
            A += 1
        elif DNA_list[j][i] == 'T':
            T += 1
        elif DNA_list[j][i] == 'G':
            G += 1
        else:
            C += 1
    # 해밍 합이 가장 적은 것 => 각 위치 해당 개수가 많은 것 택해야함
    # 그래야 해밍 거리가 적기 때문이다.
    max_dna = max(A, T, G, C)
    # 조건문을 사전순으로 미리 정한다.
    if max_dna == A:
        ans += 'A'
        h_dis += (T+G+C)
    elif max_dna == C:
        ans += 'C'
        h_dis += (A+T+G)
    elif max_dna == G:
        ans += 'G'
        h_dis += (A+T+C)
    else:
        ans += 'T'
        h_dis += (A+C+G)

print(ans)
print(h_dis)

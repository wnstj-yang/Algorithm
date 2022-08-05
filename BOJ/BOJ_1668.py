# Baekjoon Online Judge - 1668번. 트로피 진열

N = int(input())
trophies = []
for _ in range(N):
    height = int(input())
    trophies.append(height)

left = trophies[0]
right = trophies[-1]
l_cnt, r_cnt = 1, 1
# 왼쪽이나 오른쪽에서 보든 트로피가 첫 높이보다 크다면 갱신하면서 더 높은 것들을 찾는다. 눈에 보이는 거기 때문에
for i in range(1, N):
    if left < trophies[i]:
        l_cnt += 1
        left = trophies[i]
        
for i in range(N - 1, -1, -1):
    if right < trophies[i]:
        r_cnt += 1
        right = trophies[i]
print(l_cnt)
print(r_cnt)

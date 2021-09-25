# Baekjoon Online Judge - 1446번. 지름길

N, D = map(int, input().split())
# D까지의 거리
dist = list(range(D+1))
pos = [[] for _ in range(10001)]
for _ in range(N):
    s, e, w = map(int, input().split())
    pos[s].append((e, w))

for i in range(D+1):
    # 지름길이 없는 곳과 있어도 최소가 아닐 수 있으니
    # 이전 거리까지에서 현재까지 + 1해준 것과 현재 거리까지의 최소를 구한다
    if i > 0:
        dist[i] = min(dist[i], dist[i-1]+1)
    for e, w in pos[i]:
        # 범위 넘어선 것 + 최소 거리인지 판단
        if e <= D and dist[e] > w + dist[i]:
            dist[e] = w + dist[i]
print(dist[D])
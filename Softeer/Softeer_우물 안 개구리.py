# Softeer 우물 안 개구리


N, M = map(int, input().split())
weights = list(map(int, input().split()))
linked = [[] for _ in range(N)]  # 연결 상태

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    # 연결을 할 때 무게를 넣어준다.
    linked[x].append(weights[y])
    linked[y].append(weights[x])

total = 0
for i in range(N):
    # 혼자라면 그 것이 최대
    if len(linked[i]) == 0:
        total += 1
    # 연결된 회원들의 무게들을 넣어놔서 그 중에서 가장 큰 값이 현재 회원의 무게랑 비교
    elif weights[i] > max(linked[i]):
        total += 1
print(total)

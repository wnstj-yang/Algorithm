# Baekjoon Online Judge - 14267번. 회사 문화 1

from collections import deque


N, M = map(int, input().split())
boss = [0] + list(map(int, input().split())) # 1번이 사장(직원 N명의 직속 상사 번호)

W = [0] * (N + 1) # 칭찬 수치

for _ in range(M):
    i, w = map(int, input().split())
    W[i] += w

juniors = [[] for _ in range(N + 1)] # 각 직원의 부하직원들 리스트
for i in range(2, N + 1):
    juniors[boss[i]].append(i)

q = deque([1]) # 1번부터 출발
while q:
    senior = q.popleft()
    for junior in juniors[senior]:
        # 현재 상사의 칭찬 값을 부하직원에게 더해준다.
        W[junior] += W[senior]
        q.append(junior)
print(*W[1:])

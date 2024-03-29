# Baekjoon Online Judge - 1158번. 요세푸스 문제


from collections import deque

N, K = map(int, input().split())
q = deque(range(1, N + 1))

ans = []
while q:
    for _ in range(K - 1):
        q.append(q.popleft())
    ans.append(str(q.popleft()))
result = '<' + ', '.join(ans) + '>'
print(result)

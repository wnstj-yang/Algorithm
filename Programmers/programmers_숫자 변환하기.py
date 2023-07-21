# 기존에 재귀방식으로 진행했다. 제한 사항에 <= 1,000,000을 보지 않고 그냥 짜다보니 시간초과 발생
# 백트래깅을 진행해도 일단은 그냥 BFS로 돌림
# 해당 방법도 역으로 거꾸로 x -> y만들기가 아니라 y -> x로 만든다.

from collections import deque


def solution(x, y, n):
    global answer
    answer = 0
    q = deque()
    q.append((y, 0))
    while q:
        result, cnt = q.popleft()
        if result == x:
            answer = cnt
            return cnt

        if result > x:
            q.append((result - n, cnt + 1))
            # 아래 나눌 때는 나머지 연산으로 0으로 확실히 나눠지는지 파악해서 값을 큐에 넣는다
            if result % 2 == 0:
                q.append((result // 2, cnt + 1))
            if result % 3 == 0:
                q.append((result // 3, cnt + 1))

    return -1

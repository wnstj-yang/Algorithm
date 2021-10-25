# Baekjoon Online Judge - 1966번. 프린터 큐

from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    q = deque()
    ans = 0
    temp = list(map(int, input().split()))
    #  큐의 앞의 값은 중요도, 뒤의 i는 몇 번째인지 판단한다
    for i in range(N):
        q.append((temp[i], i))
    while True:
        # FIFO
        num, idx = q.popleft()
        check = True
        # 큐 안의 값 중에 중요도가 큰 것이 있다면 뒤에 추가해준다
        for item in q:
            if item[0] > num:
                check = False
                q.append((num, idx))
                break
        # 중요도가 없다면 큐에서 빠져나온다
        if check:
            ans += 1
            # 빠져나온 개수에서 뽑으려는 몇 번째가 맞으면 끝
            if idx == M:
                break
    print(ans)



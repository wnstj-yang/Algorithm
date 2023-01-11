# Baekjoon Online Judge - 13335번. 트럭

from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * w)
time = 0
while bridge:
    bridge.popleft()
    time += 1
    if trucks:
        if trucks[0] + sum(bridge) <= L:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
print(time)


# Baekjoon Online Judge - 1547번. 공

M = int(input())

cups = list(range(4))
# 컵의 위치를 뒤바꾸면서 어차피 공이 1번에 있기 때문에 다 옮긴 후 1의 위치를 찾으면 된다.
for _ in range(M):
    x, y = map(int, input().split())
    cups[x], cups[y] = cups[y], cups[x]
print(cups.index(1))

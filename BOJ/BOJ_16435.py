# Baekjoon Online Judge - 16435번. 스네이크버드

N, L = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
for h in heights:
    if L >= h:
        L += 1
    else:
        break
print(L)

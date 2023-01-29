# Baekjoon Online Judge - 14720번. 우유 축제

isAvailable = 0

N = int(input())
stores = list(map(int, input().split()))
result = 0
for i in stores:
    if isAvailable == i:
        result += 1
        isAvailable = (isAvailable + 1) % 3
print(result)
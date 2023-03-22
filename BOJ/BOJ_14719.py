# Baekjoon Online Judge - 14719번. 빗물

H, W = map(int, input().split())
heights = list(map(int, input().split()))
result = 0
# 물이 고이려면 양 옆에 높이가 있어야한다.
for i in range(1, W - 1):
    left = max(heights[:i])
    right = max(heights[i:])
    critical = min(left, right)
    if heights[i] < critical:
        result += (critical - heights[i])
print(result)

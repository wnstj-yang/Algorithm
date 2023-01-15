# Baekjoon Online Judge - 17608번. 막대기
# pypy 통과


N = int(input())
heights = []
result = 0
height = 0
for _ in range(N):
    heights.append(int(input()))
for i in range(N - 1, -1, -1):
    if height < heights[i]:
        result += 1
        height = heights[i]
print(result)

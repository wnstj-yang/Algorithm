# Baekjoon Online Judge - 2217번. 로프
import sys
input = sys.stdin.readline


N = int(input())
numbers = []
answer = 0
cnt = 1
for _ in range(N):
    numbers.append(int(input()))
numbers.sort(reverse=True)
# 내림차순으로 정렬 후 길이만큼 해당 수를 곱함
# 최대 값 = 해당 값 * 길이
for num in numbers:
    answer = max(answer, num * cnt)
    cnt += 1
print(answer)

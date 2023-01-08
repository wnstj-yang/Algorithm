# Baekjoon Online Judge - 11004번. K번째 수

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[K - 1])

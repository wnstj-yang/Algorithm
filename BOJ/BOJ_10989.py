# Baekjoon Online Judge - 10989번. 수 정렬하기 3
import sys
# 메모리 제한이 낮음

N = int(sys.stdin.readline())
# N의 수는 1부터 1000만 이하이나
# 각 수는 10000보다 작거나 같은 자연수이므로 1~10000의 수 리스트 생성
numbers = [0] * 10001

for _ in range(N):
    numbers[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numbers[i] > 0:
        while numbers[i] > 0:
            print(i)
            numbers[i] -= 1

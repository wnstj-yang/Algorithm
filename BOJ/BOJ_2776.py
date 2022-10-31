# Baekjoon Online Judge - 2776번. 암기왕

import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    M = int(input())
    target = list(map(int, input().split()))
    answer = []
    for num in target:
        left, right = 0, N - 1
        found = False
        while left <= right:
            mid = (left + right) // 2
            if num == numbers[mid]:
                found = True
                break
            # 찾고자 하는 값이 현재 값 보다 작다면 값의 범위를 줄인다.
            if num < numbers[mid]:
                right = mid - 1
            # 찾고자 하는 값이 현재 값 보다 크다면 값의 범위를 늘린다.
            else:
                left = mid + 1

        if found:
            answer.append(1)
        else:
            answer.append(0)

    for i in answer:
        print(i)

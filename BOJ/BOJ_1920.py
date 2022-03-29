# Baekjoon Online Judge - 1920번. 수 찾기

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
targets = list(map(int, input().split()))
for target in targets:
    start = 0
    end = len(numbers) - 1
    check = True
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            check = False
            print(1)
            break
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if check:
        print(0)

# Baekjoon Online Judge - 10815번. 숫자 카드

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
answer = []
numbers.sort() # 이진 탐색에 있어 정렬을 해준다
for target in targets:
    start, end = 0, N - 1
    check = True
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            answer.append(1)
            check = False
            break
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if check:
        answer.append(0)
print(*answer)

# 이분 탐색 - 부품 찾기 197p


def binary_search(arr, target, start, end):
    if start > end:
        return False
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

arr.sort()
for num in targets:
    if binary_search(arr, num, 0, len(arr) - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 5
# 8 3 7 9 2
# 3
# 5 7 9
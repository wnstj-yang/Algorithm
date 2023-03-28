# 유형별 - 이분탐색 367p - 정렬된 배열에서 특정 수의 개수 구하기

def first(arr, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
        return mid
    # 중간값이 목표값보다 크거나 같다고 해주어야 한다.
    # 같다는 표시를 하지 않을 경우 현재 같은 값이라도 왼쪽 인덱스를 찾아야 하는 상황이지만
    # 그렇지 않을 경우 값이 크거나 같다고 다르게 판단하여 오히려 오른쪽으로 가게 된다.
    elif arr[mid] >= target:
        return first(arr, left, mid - 1)
    else:
        return first(arr, mid + 1, right)


def last(arr, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if (mid == N - 1 or target < arr[mid + 1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return last(arr, left, mid - 1)
    else:
        return last(arr, mid + 1, right)


N, target = map(int, input().split())
numbers = list(map(int, input().split()))

start = first(numbers, 0, N - 1)
end = last(numbers, 0, N - 1)
if not start or not end:
    print(-1)
else:
    print(end - start + 1)



# 7 2
# 1 1 2 2 2 2 3
#
# 7 4
# 1 1 2 2 2 2 3
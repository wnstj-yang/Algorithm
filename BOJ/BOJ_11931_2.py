# Baekjoon Online Judge - 11931번. 수 정렬하기 4
# 병합정렬에서 sys로 사용했을 때 시간이 확 줄긴 하나 입출력 input을 사용해도 통과는 한다. => pypy3
import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 리스트 크기가 1이 될 때 까지 분할
    left = merge_sort(left)
    right = merge_sort(right)

    # 병합
    return merge(left, right)


def merge(left, right):
    # 분할된 리스트 합치는 결과물
    result = []
    l, r = 0, 0
    # 내림차순으로 정렬해야함
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    # 왼쪽, 오른쪽 남은 원소들을 추가한다.
    result += right[r:]
    result += left[l:]

    return result


N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

ans = merge_sort(numbers)
for i in ans:
    print(i)

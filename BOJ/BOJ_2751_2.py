# Bakejoon Online Judge - 2751번. 수 정렬하기 2 -> Quick sort

# !! Quick sort의 경우 최악이 O(N^2)이기 때문에 알고리즘 문제풀이 시 적절하진 않다
# 다만, 퀵 정렬 연습으로 해당 코드를 올리고자 한다. => 제출할 시 RecursionError

def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)


def partition(arr, start, end):
    pivot = (start + end) // 2
    L, R = start, end
    # L과 R이 교차되지 않을때 까지
    while L < R:
        # pivot기준 왼쪽은 값이 작아야 하기 때문에 pivot보다 크거나 같은 값을 찾아야한다.
        # 즉, pivot보다 작다면 L위치 증가
        while arr[L] < arr[pivot] and L < R:
            L += 1
        # pivot기준 오른쪽은 값이 커야하기 때문에 pivot보다 작은 값을 찾아야 한다.
        # 즉, pivot보다 크거나 같으면 R 위치 감소
        while arr[R] >= arr[pivot] and L < R:
            R -= 1
        # 교환
        if L < R:
            # L이 pivot값이면 pivot을 R값으로 바꾼다
            # L < R이고 L == pivot일 때 L과 R을 교환하면 제대로된 정렬이 이루어지지 않는다.
            # pivot의 값을 바꾸기 때문. 그래서 R을 pivot에 넣고 정렬을 이어나간다.
            if L == pivot:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]
        else:
            break
    # 위의 교환이 끝나면 마지막 교환
    # R교환은 0~R, R+1부터 마지막으로 생각
    arr[R], arr[pivot] = arr[pivot], arr[R]
    return R


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

quick_sort(arr, 0, len(arr) - 1)
for num in arr:
    print(num)

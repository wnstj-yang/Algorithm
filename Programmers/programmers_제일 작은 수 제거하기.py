def solution(arr):
    # 배열 arr의 최소값이 존재하는 index를 pop한다.
    arr.pop(arr.index(min(arr)))
    if len(arr) == 0:
        arr.append(-1)
    return arr
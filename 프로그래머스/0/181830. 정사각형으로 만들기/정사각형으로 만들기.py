def solution(arr):
    answer = [[]]
    N, M = len(arr), len(arr[0])
    if N > M:
        for a in arr:
            a.extend([0] * (N - M))
    elif N < M:
        for _ in range(M - N):
            arr.append([0] * M)

    return arr
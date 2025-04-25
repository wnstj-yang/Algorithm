def solution(A, B):
    answer = 0
    cnt = 0
    while cnt < len(A):
        if A == B:
            answer = cnt
            break
        A = A[-1] + A[:-1]
        cnt += 1
    if A != B:
        answer= -1
    return answer
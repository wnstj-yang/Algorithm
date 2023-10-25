def solution(A, B):
    answer = 0
    # 출전 순서를 알지만, 서로 내림차순 정렬을 진행해서 큰 값으로 처리가 가능한지 파악한다.
    A.sort(reverse=True)
    B.sort(reverse=True)
    for a in A:
        # 맨 앞이 가장 큰 값이므로 B에서 a보다 크다면 pop
        if a < B[0]:
            B.pop(0)
            answer += 1
    return answer

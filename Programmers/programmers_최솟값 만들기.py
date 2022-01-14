def solution(A,B):
    answer = 0
    # A와 B 리스트안의 값들을 한칸씩 옮기면서 하기엔 시간 초과
    # 예를 들어 A는 그대로 B 값들 곱하고 한칸씩 옮기면서 진행
    # 그래서 A에는 오름차순 정렬, B에는 내림차순 정렬 후 곱하여 최솟값을 구한다
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
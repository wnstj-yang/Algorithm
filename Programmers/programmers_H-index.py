def solution(citations):
    answer = 0
    citations.sort()
    # 3 0 6 1 5 => 0 1 3 5 6

    # citations[h]는 h번 논문이 인용된 횟수이고 len(citations[h:])는 인용된 논문의 개수를 의미
    # 최댓값부터 하나씩 줄여나간 것이다. (최댓값을 찾아야 하므로 가장 큰 값부터 시작)
    # 그리고 리스트는 오름차순 정렬된 상태이므로 h번째 이후는 모두 h번째보다 큰 값을 가질 것이다.
    for h in range(len(citations)):
        # 각 자리는 논문 인용된 횟수 h >= 논문 인용된 횟수가 h편 이상(최대값을 구함)
        # h번 논문이 인용된 횟수 오름차순 정렬이여서 부등호 >=
        if citations[h] >= len(citations[h:]):
            answer = len(citations[h:])
            break

    return answer
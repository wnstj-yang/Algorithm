def solution(citations):
    answer = 0
    citations.sort()
    length = len(citations)
    for i in range(length):
        h = citations[i]
        # h => h번 이상 인용된 논문이 h편 이상
        if h >= len(citations[i:]):

            answer = len(citations[i:])
            break
    return answer

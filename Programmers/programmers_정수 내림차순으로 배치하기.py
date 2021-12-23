def solution(n):
    answer = []
    while n > 0:
        # 저장을할 때 string으로
        answer.append(str(n % 10))
        n = n // 10
    # 내림차순으로 정렬 후
    answer.sort(reverse=True)
    # 정수로 바꿔서 반환
    return int(''.join(answer))
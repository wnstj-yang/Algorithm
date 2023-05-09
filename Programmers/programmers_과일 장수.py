def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)  # 내림차순 정렬으로 최대 값을 구하도록 진행
    idx = 0  # 개수 파악을 위한 인덱스
    while True:
        box = score[idx:idx + m]  # 내림차순 정렬된 상태에서 현재 인덱스부터 m개의 길이가 더해진 수들을 구한다
        if len(box) == m:  # 길이가 m개면 상자가 완성된 상태이므로 아래 계산을 진행한다
            answer += min(box) * m  # 상자의 최소 값과 상자 안의 개수인 m을 곱해서 이익을 더해준다
            idx = idx + m  # 인덱스의 갱신
        else:
            break

    return answer

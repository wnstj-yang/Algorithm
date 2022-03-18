def solution(N, stages):
    answer = {}
    stage_cnt = {}
    length = len(stages)
    for i in range(1, N + 1):
        stage_cnt[i] = stages.count(i)
    for key, val in stage_cnt.items():
        # 나누려고 하는 스테이지에 도달한 플레이어 수가 0인 경우 런타임 에러 방지
        # 0으로 초기화
        if length == 0:
            answer[key] = 0
            continue
        # 이외에의 경우 실패율을 넣어서 저장한다.
        answer[key] = val / length
        length -= val
    # 딕셔너리 정렬 방식으로 실패율에 따라 내림차순 정렬을 진행한다.
    answer = sorted(answer.items(), key = lambda x:x[1], reverse=True)
    result = []
    # 정렬 이후 key 부분만을 저장해서 리턴
    for num in answer:
        result.append(num[0])

    return result
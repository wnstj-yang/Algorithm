def solution(id_list, report, k):
    answer = {}
    result = {}
    for name in id_list:
        answer[name] = 0
    # 신고를 당했던 사람 : 신고를 한 사람 형태로 저장
    for names in report:
        x, y = names.split(' ')
        if y not in result:
            result[y] = [x]
        else:
            # 중복 방지 (set으로 진행이 안됨)
            if x not in result[y]:
                result[y].append(x)
    # 만들어진 결과물에서 k에 만족하는 경우 각 신고한 사람에게 정지 알림을 해야해서 증가
    for key, value in result.items():
        if len(value) >= k:
            for name in result[key]:
                answer[name] += 1

    answer = list(answer.values())
    return answer

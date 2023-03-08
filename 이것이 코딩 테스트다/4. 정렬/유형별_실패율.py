# 정렬 - 유형별. 실패율 361p

def solution(N, stages):
    answer = {}
    people = len(stages)
    for i in range(1, N + 1):
        if people == 0:
            answer[i] = 0.0
            continue
        cnt = stages.count(i)
        answer[i] = cnt / people
        people -= cnt
    sorted_answer = sorted(answer.items(), key=lambda x:-x[1])
    result = []
    for key, val in sorted_answer:
        result.append(key)
    return result

def solution(priorities, location):
    answer = 1
    q_indexs = list(range(len(priorities)))
    while True:
        if priorities[0] >= max(priorities):
            if q_indexs[0] == location:
                break
            q_indexs.pop(0)
            priorities.pop(0)
            answer += 1
        else:
            q_indexs.append(q_indexs.pop(0))
            priorities.append(priorities.pop(0))

    return answer

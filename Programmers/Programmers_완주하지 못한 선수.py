def solution(participant, completion):
    comp_list = {}
    answer = ''
    # 해당 참가자를 동명이인 파악위해 딕셔너리로 명수 파악
    for name in participant:
        if name not in comp_list:
            comp_list[name] = 1
        else:
            comp_list[name] += 1
    # 완주한 사람들을 파악해 수를 명수를 줄여나간다
    for name in completion:
        comp_list[name] -= 1

    # 완주하지 못한 사람을찾는다
    for name in comp_list:
        if comp_list[name] == 1:
            answer = name
            break
    return answer
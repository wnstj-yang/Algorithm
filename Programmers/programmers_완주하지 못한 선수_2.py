def solution(participant, completion):
    answer = ''
    result = participant + completion
    part_list = {}
    for name in result:
        if name in part_list:
            part_list[name] += 1
        else:
            part_list[name] = 1
    for key, val in part_list.items():
        if val % 2 == 1:
            answer = key
            break
    return answer
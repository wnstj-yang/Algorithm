def solution(clothes):
    answer = 1
    clothes_dict = {}
    for clothe in clothes:
        if clothe[1] not in clothes_dict:
            clothes_dict[clothe[1]] = 2 # 항목 + 안입는 것. 즉, 일종의 여집합
        else:
            clothes_dict[clothe[1]] += 1
    for val in clothes_dict.values():
        answer *= val
    # 모두 안입는 경우 1개를 빼준다
    return answer - 1

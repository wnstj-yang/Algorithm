def solution(clothes):
    answer = 1
    clothes_dict = {}
    # 경우의 수 문제
    for cloth in clothes:
        if cloth[1] not in clothes_dict:
            # 안입는 경우까지 포함해서 + 1해야함
            clothes_dict[cloth[1]] = 2
        else:
            clothes_dict[cloth[1]] += 1

    # 각 의상의 수를 곱해준다 (경우의 수)
    for val in clothes_dict.values():
        answer *= val
    # 모두 안입는 경우는 빼야 하므로 return 시 - 1
    return answer - 1
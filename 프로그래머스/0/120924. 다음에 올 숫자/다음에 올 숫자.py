def solution(common):
    # 길이가 3이상이고, 같으면 등차수열, 다르면 등비수열이다.
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1] // common[0])
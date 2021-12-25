def solution(s):
    length = len(s)
    answer = s.isdigit()
    # 문자열 길이가 4 혹은 6이여야 하므로 나머지는 False
    if length != 4 and length != 6:
        answer = False
    return answer
def solution(strings, n):
    answer = []
    # 사전순으로 문자열을 먼저 정렬한 후에
    strings.sort()
    # 이어 받아 각 문자열 n번째의 수에 따라 다시 정렬을 해준다
    strings.sort(key=lambda x: x[n])
    return strings
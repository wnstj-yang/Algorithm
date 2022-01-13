def solution(s):
    answer = []
    depth, cnt = 0, 0  # 회차 및 0의 개수
    while len(s) > 1:
        only_ones = ''
        cnt_zero = 0
        for i in s:
            if i == '1':
                only_ones += '1'
            else:
                cnt_zero += 1
        cnt += cnt_zero
        next = bin(len(only_ones))  # 0 제거 후 길이를 바이너리로
        s = next[2:]  # 문자열로 0b110 이런식으로 반환이 되므로 리스트 슬라이싱 적용하여 110만 넘긴다
        depth += 1
    answer = [depth, cnt]

    return answer
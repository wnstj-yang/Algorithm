# 323p 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    answer = ''
    min_cnt = 987654321
    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        prev = s[:i]
        temp = ''
        for j in range(i, len(s), i):
            if s[j:i + j] == prev:
                cnt += 1
            else:
                if cnt != 1:
                    temp += (str(cnt) + prev)
                else:
                    temp += prev
                prev = s[j:i + j]
                cnt = 1
        # 마지막 남은 부분을 더해준다.
        if cnt != 1:
            temp += (str(cnt) + prev)
        else:
            temp += prev
        min_cnt = min(min_cnt, len(temp))

    if min_cnt == 987654321:
        min_cnt = 1

    return min_cnt

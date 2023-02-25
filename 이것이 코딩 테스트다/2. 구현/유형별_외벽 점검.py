# 구현 - 유형별 문제. 외벽 점검 / 335p
# https://school.programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    weak = weak + [n + i for i in weak]  # 원형을 2배하여 1줄로 만드는 방법
    for idx in range(length):
        # 1부터 N까지의 순열이 아닌 N개의 순열을 구한 후 count하는 식
        for item in permutations(dist, len(dist)):
            cnt = 1
            now = weak[idx] + item[cnt - 1]  # 현재 위치값
            for i in range(idx, idx + length):
                if now < weak[i]:  # weak의 현재 위치가 현재 위치인 now 보다 크다면 친구를 추가하여 점검
                    cnt += 1
                    if cnt > len(dist):
                        break
                    now = weak[i] + item[cnt - 1]
            answer = min(answer, cnt)

    if answer == len(dist) + 1:
        answer = -1

    return answer

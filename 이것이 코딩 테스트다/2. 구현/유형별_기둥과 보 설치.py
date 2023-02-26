# 구현 유형별 문제 - 기둥과 보 설치
# https://school.programmers.co.kr/learn/courses/30/lessons/60061


def check(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for info in build_frame:
        # 가로, 세로, 구조물 종류, 설치 or 삭제 여부
        x, y, stuff, state = info
        if state == 0: # 삭제
            answer.remove([x, y, stuff])
            if not check(answer):
                answer.append([x, y, stuff])
        else: # 추가
            answer.append([x, y, stuff])
            if not check(answer):
                answer.remove([x, y, stuff])

    answer.sort()
    return answer

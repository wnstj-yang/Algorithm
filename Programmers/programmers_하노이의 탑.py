def hanoi(circle, depart, via, arrive, answer):
    if circle == 1:  # 원반 하나일 때 시작 기둥에서 도착 기둥
        return answer.append([depart, arrive])
    hanoi(circle - 1, depart, arrive, via, answer)  # 1번 기둥에 있는 원반들을 2번으로(3번 기둥 보조)
    answer.append([depart, arrive])  # 가장 큰 원반 이동(1번 기둥에 남아있는)
    hanoi(circle - 1, via, depart, arrive, answer)  # 2번 기둥에 있는 원반들을 3번으로(1번 기둥 보조)


def solution(n):
    # n개의 원판 -> 그냥 쭉 오른쪽으로 넘기기 시작
    answer = []
    hanoi(n, 1, 2, 3, answer)

    return answer
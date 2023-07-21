from copy import deepcopy


def solution(want, number, discount):
    answer = 0
    need = {}  # 원하는 제품의 개수
    # 각 개수에 맞게 딕셔너리로
    for i in range(len(want)):
        need[want[i]] = number[i]
    # 각 인덱스마다 10개를 돌아야하기 때문에 전체 길이 - 10개 + 1 (인덱스 판단으로 1 추가)
    for i in range(len(discount) - 10 + 1):
        need_copy = deepcopy(need)  # 개수파악을 위해 복사
        for j in range(10):
            key = discount[i + j]
            # key가 있고 0보다 큰 경우라면 1을 줄이면서 개수 파악
            if key in need_copy and need_copy[key] > 0:
                need_copy[key] -= 1
        # 순회한 이후 값이 모두 0이면 전부 조건에 맞기 때문에 가능하다고 파악하여 1 증가
        if sum(need_copy.values()) == 0:
            answer += 1

    return answer

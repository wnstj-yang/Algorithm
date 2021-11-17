def solution(d, budget):
    answer = 0
    # 정렬을 해서 최소 금액부터 예산을 깎는다.
    d.sort()
    for item in d:
        # 지원을 해줄 수 있는지 미리 예산을 빼서 확인
        if budget - item >= 0:
            # 가능하면 지원해주고 예산을 깎는다.
            answer += 1
            budget -= item
        else:
            # 예산이 없다면 끝 (오름차순 정렬을 했기 때문)
            break
    return answer
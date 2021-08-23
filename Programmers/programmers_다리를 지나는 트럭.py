def solution(bridge_length, weight, truck_weights):
    # sum() 부분에서 시간이 좀 걸린다
    answer = 0
    # queue에 길이만큼 곱해줘서 시간을 count / 사실상 stack
    queue = [0] * bridge_length
    while queue:
        answer += 1
        queue.pop(0)
        if truck_weights:
            # 견딜 수 있는 무게를 초과하지 않는다면 그 다음 트럭 추가
            if truck_weights[0] + sum(queue) <= weight:
                queue.append(truck_weights.pop(0))
            # 초과하면 시간을 추가(트럭이 못올라감) / 위에서 pop
            else:
                queue.append(0)

    return answer
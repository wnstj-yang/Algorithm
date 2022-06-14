def solution(tickets):
    answer = []
    flight_state = {}
    for a, b in tickets:
        if a not in flight_state:
            flight_state[a] = [b]
        else:
            flight_state[a].append(b)
    # 내림차순으로 정렬하는 이유는 예외에 대한 처리를 위함
    for key in flight_state.keys():
        flight_state[key].sort()
    stack = ['ICN']
    while stack:
        now = stack[-1] # 현재위치를 갱신
        # 항공편에 없는 경우 혹은 다 돌았을 때면 stack 값 제거
        if now not in flight_state or len(flight_state[now]) == 0:
            answer.append(stack.pop())
        else:
            # 있다면 추가해주고 해당 항공편은 방문처리헀다는 의미로 pop
            stack.append(flight_state[now][0])
            flight_state[now].pop(0)
    # stack형태로 있는 값들을 역순으로 돌려서 순서를 정렬한다
    answer.reverse()
    return answer

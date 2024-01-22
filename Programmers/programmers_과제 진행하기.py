def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = plans[i][1].split(':')
        plans[i][1] = int(h) * 60 + int(m)
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    stack = []
    # 각 과제 완료시간까지의 합으로 진행할 경우 문제에서 끝낸 시각에 새로 시작, 멈춰둔 과제 모두 존재할 경우
    # 멈춰둔 과제를 진행하게 되고 설령 수정하더라도 코드가 더 복잡해 보이기 때문에 아래와 같이 gap을 활용
    for i in range(len(plans) - 1):
        stack.append([plans[i][0], plans[i][2]])  # 이름, 걸리는 시간
        gap = plans[i + 1][1] - plans[i][1]  # 다음 시작 시간 - 현재 시작 시간
        while stack and gap:
            # 최근 과제의 걸리는 시간이 gap보다 작거나 같은 경우에는 최근 과제를 끝낼 수 있다.
            if stack[-1][1] <= gap:
                name, time = stack.pop()
                gap -= time  # 과제 시간을 빼면서 진행 상황 체크
                answer.append(name)
            # 그렇지 못한 경우 최근과제가 완료될 시간까지의 남은 시간을 보여주므로 아래와 같이gap을 뺴준다
            else:
                stack[-1][1] -= gap  # 다음 과제를 넘어갔을 때 stack에 들어가있는 최근 과제의 시간을 빼준다
                gap = 0
    answer.append(plans[-1][0])  # 마지막 과제
    # stack에 남아있는 과제들 추가
    while stack:
        name, time = stack.pop()
        answer.append(name)

    return answer

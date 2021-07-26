def solution(progresses, speeds):
    answer = []
    # 배포 되는 날들 리스트
    deploy_days = []
    for i in range(len(progresses)):
        # 100에서 뺀 다음 몇이나 부족한지 체크
        result = 100 - progresses[i]
        # 딱 나누어지는 경우랑 아닌 경우의 배포날 차이
        if result % speeds[i] != 0:
            result = result // speeds[i] + 1
        else:
            result = result // speeds[i]
        deploy_days.append(result)

    idx = 1
    cnt = 1
    # 현재 배포되는 작업의 위치
    value = 0
    while idx < len(deploy_days):
        # 현재 배포날 보다 다음 배포날이 작거나 같은 경우 일 수와 위치 이동
        if deploy_days[value] >= deploy_days[idx]:
            cnt += 1
            idx += 1
        # 현재 배포날에 기능이 다 포함되는 곳까지 갔다면 answer에 넣음
        else:
            value = idx
            idx += 1
            answer.append(cnt)
            cnt = 1
    # 하나만 나오는 경우 및 맨 마지막에서 이전까지 간 경우니 뒤에 한 번 더 카운트해준다
    answer.append(cnt)

    return answer
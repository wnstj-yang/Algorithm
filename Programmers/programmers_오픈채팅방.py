def solution(record):
    answer = []
    friends = {}
    # 처음에 들어왔는지 나갔는지에 대해 id값에 따라 이름을 더해준다
    for info in record:
        info = list(info.split())
        if info[0] == 'Enter' or info[0] == 'Change':
            friends[info[1]] = info[2]
    # 두 번째로는 들어왔는지 나갔는지 최종적으로 만들어진 이름으로 리스트 생성
    for info in record:
        info = list(info.split())
        if info[0] == 'Enter':
            answer.append(f'{friends[info[1]]}님이 들어왔습니다.')
        elif info[0] == 'Leave':
            answer.append(f'{friends[info[1]]}님이 나갔습니다.')

    return answer
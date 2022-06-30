def solution(n, t, m, timetable):
    answer = ''
    # 모두 분으로 환산
    n_timetable = []
    for time in timetable:
        time = int(time[:2]) * 60 + int(time[3:])
        n_timetable.append(time)
    n_timetable.sort()  # 정렬

    # 버스와 크루 도착 시간을 리스트로 만들어서 판단
    bus_table = [540 + t * i for i in range(n)]
    idx = 0
    for bus in bus_table:
        crew = 0
        # 크루가 최대 수용 m명을 넘지 않고, 인덱스 넘지 않고, 크루 도착 시간이 버스 시간보다 작거나 같을 때
        while crew < m and idx < len(n_timetable) and n_timetable[idx] <= bus:
            crew += 1
            idx += 1

        # 셔틀에 빈 자리가 존재한 경우
        if crew < m:
            answer = bus
        # 셔틀에 빈 자리가 없는 경우 / 콘이 타야됨
        # 단위가 분이므로 현재 인덱스에서 앞에있는 거에 1분 줄인다.
        else:
            answer = n_timetable[idx - 1] - 1
    # 시간, 분 구분
    hour = str(answer // 60)
    minute = str(answer % 60)
    if int(hour) < 10:
        hour = '0' + str(hour)
    if int(minute) < 10:
        minute = '0' + str(minute)
    answer = hour + ':' + minute
    return answer

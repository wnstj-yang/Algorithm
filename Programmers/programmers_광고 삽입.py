def change_to_sec(time):
    return int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:])


def change_to_time(sec):
    result = ''
    hour = sec // 3600
    if hour < 10:
        result += '0' + str(hour) + ':'
    else:
        result += str(hour) + ':'
    sec = sec % 3600
    minute = sec // 60
    if minute < 10:
        result += '0' + str(minute) + ':'
    else:
        result += str(minute) + ':'
    sec = sec % 60
    if sec < 10:
        result += '0' + str(sec)
    else:
        result += str(sec)
    return result


def solution(play_time, adv_time, logs):
    answer = ''
    # 초단위로 환산
    play_sec = change_to_sec(play_time)
    adv_sec = change_to_sec(adv_time)
    timeline = [0] * (play_sec + 1)
    # 1. logs에 시정차의 시작과 끝점에 존재함을 표시
    for time in logs:
        start = change_to_sec(time[:8])
        end = change_to_sec(time[9:])
        timeline[start] += 1  # 한 시청자의 시청 시작 표시
        timeline[end] -= 1  # 한 시청자의 시청이 끝남을 -1로 표기
    # 2. 시청자의 수를 누적
    for i in range(len(timeline) - 1):
        timeline[i + 1] += timeline[i]
    # 3. 시청시간 누적
    for i in range(len(timeline) - 1):
        timeline[i + 1] += timeline[i]
    max_time = timeline[adv_sec - 1]  # 인덱스상 0~adv_sec
    max_start = 0  # 즉, 0초부터 adv_sec까지
    for i in range(adv_sec, play_sec):
        if max_time < timeline[i] - timeline[i - adv_sec]:
            max_time = timeline[i] - timeline[i - adv_sec]
            max_start = i - adv_sec + 1  # 가장 빠른 시작 시각(adv_sec포함됨)

    answer = change_to_time(max_start)

    return answer
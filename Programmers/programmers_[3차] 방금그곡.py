def solution(m, musicinfos):
    answer = []
    max_time = 0
    idx = 0
    # 각 음에 따른 치환
    sounds = {'C#': '1', 'D#': '2', 'F#': '3', 'G#': '4', 'A#': '5'}
    for key,val in sounds.items():
        m = m.replace(key, val)

    for info in musicinfos:
        info = info.split(',')
        # 1. 분 단위로 시간을 구한다
        hour = (int(info[1][:2]) - int(info[0][:2])) * 60
        minute = (int(info[1][3:]) - int(info[0][3:]))
        time = hour + minute # 총 재생 시간
        # 2. 악보 정보 또한 치환시킨다.
        for key,val in sounds.items():
            info[3] = info[3].replace(key, val)
        # 3. 재생 시간 만큼의 연속되는 문자열을 저장
        lyrics = ''
        length = len(info[3])
        if time // length != 0:
            lyrics += info[3] * (time // length)
        end = time % length
        lyrics += info[3][:end]
        # 4. 재생 시간이 긴 것과 인덱스, 음악 제목을 넣어서 추후 정답에 활용
        if m in lyrics:
            answer.append((time, idx, info[2]))
        idx += 1

    # 5. 재생 시간 긴 것 - 내림 차순, 인덱스 - 오름 차순으로 정렬해서 정답 찾는다.
    if len(answer) == 0:
        return "(None)"
    else:
        answer.sort(key=lambda x:(-x[0], x[1]))
        return answer[0][2]


def solution(lines):
    answer = 0
    timeline = []
    for line in lines:
        date, S, T = line.split(' ')
        S = S.split(':')
        end = int((int(S[0]) * 3600 + int(S[1]) * 60 + float(S[2])) * 1000)  # 단위를 msec로 만든 후 정수형
        T = int(float(T[:-1]) * 1000)
        start = end - T + 1
        timeline.append([start, end])

    for i in range(len(timeline)):
        cnt = 0
        end_time = timeline[i][1]
        # 각 작업의 끝난 시간을 기준으로 해서 그 다음의 작업들의 시작시간의 1초를 뺀 것이 작다면 개수 카운트
        for j in range(i, len(timeline)):
            if end_time > timeline[j][0] - 1000:
                cnt += 1
        answer = max(answer, cnt)

    return answer

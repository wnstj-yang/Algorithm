def solution(progresses, speeds):
    answer = []
    result = []
    for i in range(len(speeds)):
        percent_left = 100 - progresses[i]
        if percent_left % speeds[i] != 0:
            result.append(percent_left // speeds[i] + 1)
        else:
            result.append(percent_left // speeds[i])
    idx = 1
    cnt = 1
    val = result[0]
    while idx < len(result):
        if val >= result[idx]:
            idx += 1
            cnt += 1
        else:
            val = result[idx]
            idx += 1
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    return answer

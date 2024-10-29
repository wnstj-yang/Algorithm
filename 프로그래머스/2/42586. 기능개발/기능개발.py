def solution(progresses, speeds):
    answer = []
    left = []
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        result = 100 - p
        if result % s == 0:
            left.append(result // s)
        else:
            left.append(result // s + 1)
    cnt = 1
    max_val = left[0]

    for i in range(1, len(left)):
        if max_val >= left[i]:
            cnt += 1
        else:
            answer.append(cnt)
            max_val = left[i]
            cnt = 1
    answer.append(cnt)
    return answer
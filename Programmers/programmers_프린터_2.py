def solution(priorities, location):
    target = []
    answer = 0
    for i in range(len(priorities)):
        target.append((priorities[i], i))

    while target:
        max_prior = max(target)[0]
        prior, value = target.pop(0)
        if prior == max_prior:
            answer += 1
            if value == location:
                break
        else:
            target.append((prior, value))
    return answer
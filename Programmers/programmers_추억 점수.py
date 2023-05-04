def solution(name, yearning, photo):
    answer = []
    scores = {}
    for i in range(len(name)):
        scores[name[i]] = yearning[i]
    for team in photo:
        cnt = 0
        for member in team:
            if member in scores:
                cnt += scores[member]
        answer.append(cnt)
    return answer

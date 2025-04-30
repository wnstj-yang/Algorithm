def solution(score):
    answer = []
    score_list = []
    ranks = {}
    for x, y in score:
        score_list.append(x + y)
    score_list.sort(reverse=True)
    rank = 1
    for sum_score in score_list:
        if sum_score not in ranks:
            ranks[sum_score] = rank
        rank += 1
    for x, y in score:
        answer.append(ranks[x + y])
    return answer
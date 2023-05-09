def solution(k, score):
    answer = []
    score_list = [] # 상위 k번째 이내의 수
    for i in range(len(score)):
        score_list.append(score[i]) # k일 이전 이후이든 점수를 넣는다
        if i >= k: # k일 이후
            score_list.remove(min(score_list)) # 상위 k번째까지의 수를 가져야 하므로 최소 값을 빼준다
        answer.append(min(score_list)) # 이후 k번째 이내의 수들 중 최소값을 발표 점수로 정한다

    return answer

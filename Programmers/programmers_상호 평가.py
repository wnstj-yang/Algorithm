def solution(scores):
    answer = ''
    length = len(scores)
    # 열로 봤을 때 각각 최대랑 최소 값 구해서 자기 자신이 유일한지 판단
    for i in range(length):
        my_score = []
        for j in range(length):
            my_score.append(scores[j][i])
        max_val = max(my_score)
        min_val = min(my_score)
        # 유일한 최대값인지 혹은 최소 값인지 개수를 세고 판단한다.
        # 맞다면 해당 수를 뺀다
        if my_score[i] == max_val and my_score.count(max_val) == 1:
            my_score.pop(i)
        elif my_score[i] == min_val and my_score.count(min_val) == 1:
            my_score.pop(i)

        avg = sum(my_score) / len(my_score)

        if avg >= 90:
            answer += 'A'
        elif 80 <= avg < 90:
            answer += 'B'
        elif 70 <= avg < 80:
            answer += 'C'
        elif 50 <= avg < 70:
            answer += 'D'
        else:
            answer += 'F'

    return answer

# 프로그래머스 - 성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    orders = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0,
    }
    scores = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3,
    }
    for i in range(len(survey)):
        not_agree, agree = survey[i]
        choice = choices[i]
        if choice < 4: # 비동의 계열인 경우
            orders[not_agree] += scores[choice] # 첫 번째 알파벳의 점수로 계산
        elif choice > 4: # 동의 계열인 경우
            orders[agree] += scores[choice] # 두 번째 알파벳의 점수로 계산

    for items in ['RT', 'CF', 'JM', 'AN']:
        first, second = items # 각각 하나씩 넣음
        if orders[first] > orders[second]:
            answer += first
        elif orders[first] < orders[second]:
            answer += second
        else:
            # 같다면 사전순으로 해야하므로 최소 값을 넣는다.
            answer += min(first, second)
    return answer

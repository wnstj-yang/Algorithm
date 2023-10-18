# 프로그래머스 - 개인정보 수집 유효기간

def solution(today, terms, privacies):
    # 일(day) 단위로 모두 계산해준다
    # 월 28일로 고정되어있기 때문에 변환 후 판단
    answer = []
    terms_value = {}
    year, month, day = today.split('.')
    today = int(year) * 336 + int(month) * 28 + int(day)
    for term in terms:
        ttype, month = term.split(' ')
        terms_value[ttype] = int(month) * 28

    for i in range(len(privacies)):
        privacy = privacies[i]
        date, ttype = privacy.split(' ')
        year, month, day = date.split('.')
        result = int(year) * 336 + int(month) * 28 + int(day) + terms_value[ttype]
        # 같은 경우도 유효기간 내에 포함된다.
        if today >= result:
            answer.append(i + 1)
    return answer

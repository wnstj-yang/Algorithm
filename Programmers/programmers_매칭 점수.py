def solution(word, pages):
    answer = {}
    page_list = {}  # 링크 연결 상태 및 개수
    score = {}  # 기본 점수
    word = word.upper()  # 대문자로 통일
    # 각 웹페이지별 내용들을 대문자로 통일하고 공백으로 나눈다.
    for page in pages:
        page = page.upper()
        temp = page.split()
        length = len(word)
        result = 0
        now = ''  # 현재 웹페이지 URL
        for alpha in temp:
            idx = 0
            # 현재 웹페에지 URL을 저장
            if 'CONTENT="HTTPS://' in alpha:
                start = alpha.index('H')
                now = alpha[start:-3]
                page_list[alpha[start:-3]] = []
            # 현재 웹페이지에 연결된 외부 링크들 저장
            if 'HREF' in alpha:
                start = alpha.index('HT')
                end = alpha.index('>')
                page_list[now].append(alpha[start:end - 1])

            # 단어가 각 덩어리별로 있는 내용들에서 존재할 경우
            if word in alpha:
                while idx < len(alpha):
                    # 알파벳이 타겟 단어의 맨 앞 알파벳과 같은 경우
                    if alpha[idx] == word[0]:
                        # 그 길이랑 딱 맞는 경우
                        if alpha[idx:idx + len(word)] == word:
                            if idx + len(word) == len(word):
                                result += 1
                                idx += len(word)
                                continue
                            # 그렇지 않을 때 앞 뒤 알파벳인지 살펴보고 아니여야 맞다.
                            if idx + len(word) < len(alpha) and not alpha[idx - 1].isalpha() and not alpha[
                                idx + len(word)].isalpha():
                                result += 1
                                idx += len(word)
                            else:
                                idx += len(word)
                        else:
                            idx += len(word)
                    else:
                        idx += 1
        # 현재 웹페이지의 기본 점수
        score[now] = result

    idx = 0

    linked_state = {}  # 연결된 각 외부 링크들을 각 웹페이지에따라 누가 연결됐는지 다시 파악
    for link in page_list:
        linked_state[link] = []
        for temp_link in page_list:
            for value in page_list[temp_link]:
                if value == link:
                    linked_state[link].append(temp_link)
    # 점수내는 것
    for link in linked_state:
        link_score = 0
        for value in linked_state[link]:
            if value in linked_state:
                link_score += score[value] / len(page_list[value])

        result = score[link] + link_score
        if result not in answer:
            answer[result] = idx
        else:
            answer[result].append(idx)
        idx += 1
    # 가장 큰 값 중에 인덱스가 제일 작은 애를 리턴
    temp = [answer[max(answer)]]
    temp.sort()
    answer = temp[0]

    return answer
def solution(babbling):
    answer = 0
    bab_list = ['aya', 'ye', 'woo', 'ma']  # 옹알이 리스트
    for bab in babbling:
        for word in bab_list:  #
            if word * 2 not in bab:  # 연속발음 방지를 위해 2를 곱해서 연속되는 것이 없다면 띄워쓰기 한 칸으로 변환
                # 단순히 공백으로 하지 않는 이유는 이게 yayae처럼 발음되지 않는 경우이지만 지우면서 되는 경우로 바뀐다
                # 그래서 띄워쓰기 하나로 처리하거나 다른 문자를 추가하거나 해야된다.
                bab = bab.replace(word, ' ')
        bab = bab.replace(' ', '')  # 마지막으로 띄워쓰기들을 공백으로 처리한다.
        if len(bab) == 0:  # 길이가 0인 경우 발음할 수 있는 경우이므로 경우의 수 추가
            answer += 1

    return answer

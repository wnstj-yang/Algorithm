def solution(s):
    answer = []
    # string = "word1 word2  word3   word4    "
    # split()의 경우 공백이 몇개건 1개로 보고 처리하여 [word1, word2, word3, word4] 로 표현된다
    # 반면 split(' ')은 공백 1개를 기준으로 보기 때문에 [word1, 'word2', '', ...]식으로 표현

    words = s.split(' ')
    for word in words:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        answer.append(new_word)

    return ' '.join(answer)
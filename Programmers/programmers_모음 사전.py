# 모음들의 집합을 모두 구한다
def put_words(words, alphabets, cnt, result):
    # 단어의 길이가 5이하임
    if cnt == 5:
        return
    # 뒤에 알파벳을 추가하면서 리스트에 문자열 추가
    for alpha in alphabets:
        words.append(result + alpha)
        put_words(words, alphabets, cnt+1, result + alpha)
def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    words = [] # 모음들의 집합들을 담는 리스트
    put_words(words, alphabets, 0, '')

    return words.index(word) + 1
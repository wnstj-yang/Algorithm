# SW Expert Academy - 7675번. 통역사 성경이

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    whole = ''
    whole_cnt = 0
    end = ['!', '?', '.']
    while whole_cnt < N:
        sentence = input()
        whole += sentence
        for i in end:
            whole_cnt += sentence.count(i)
    whole = whole.split()
    cnt = 0
    answer = []
    for word in whole:
        last = word[-1]
        if last in end:
            word = word[:-1]
        # 1. 맨 앞이 대문자이며
        # 2. 길이가 1개 혹은 대문자 이후의 문자들이 모두 소문자이다
        # 3. 마지막으로 모두 알파벳인 경우에 이름의 개수 카운트
        if 65 <= ord(word[0]) <= 90 and (len(word) == 1 or word[1:].islower()) and word.isalpha():
            cnt += 1
        if last in end:
            answer.append(cnt)
            cnt = 0
    print('#{} '.format(tc), end='')
    print(*answer)

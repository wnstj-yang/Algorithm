# Baekjoon Online Judge - 1283번. 단축키 지정

N = int(input())
visited = [False] * 26
for _ in range(N):
    # 단어 공백기준
    words = input()
    # split을 통해 공백 기준으로 리스트를 만든다.(단어가 공백인 경우도 존재... 문제에는 내용이 있는지 잘 모르겠다)
    check_words = words.split(' ')
    check = True
    # 1. 첫 글자를 비교를 해준다
    for i in range(len(check_words)):
        # 공백 건너뜀
        if check_words[i] == '':
            continue
        else:
            # 알파벳이 옵션에 해당되지 않는다면
            if not visited[ord(check_words[i][0].upper()) - 65]:
                visited[ord(check_words[i][0].upper()) - 65] = True
                # 표시해주고 붙여준다
                check_words[i] = '[' + check_words[i][0] + ']' + check_words[i][1:]
                print(' '.join(check_words))
                check = False
                break
    # 첫 글자가 이미 각 단어마다 지정됐을 경우 왼쪽에서부터 오른쪽으로 지정
    if check:
        last = True
        for i in range(len(words)):
            if words[i] == ' ':
                continue
            else:
                if not visited[ord(words[i].upper()) - 65]:
                    visited[ord(words[i][0].upper()) - 65] = True
                    temp = words[:i] + '[' + words[i] + ']' + words[i+1:]
                    print(temp)
                    last = False
                    break
        if last:
            print(words)

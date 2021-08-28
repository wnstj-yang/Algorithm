# Baekjoon Online Judge - 6550번. 부분 문자열
# Python EOF 처리 ! 그리고 출력어떤건지 제대로 보기

while True:
    try:
        s, t = map(str, input().split())
        s_idx, t_idx = 0, 0
        s_length = len(s)
        t_length = len(t)
        # 답을 찾았는지 확인하는 flag
        check = False
        # t의 인덱스를 끝까지 확인
        while t_idx < t_length:
            # 부분문자열 중 같은 문자가 있으면 s, t 둘 다 인덱스 증가
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                t_idx += 1
            # 아니라면 t의 인덱스만 증가
            else:
                t_idx += 1
            # 다 찾았다면 정답
            if s_idx == s_length:
                check = True
                break

        if check:
            print('Yes')
        else:
            print('No')
    except:
        break

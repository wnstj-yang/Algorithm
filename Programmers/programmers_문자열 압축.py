def solution(s):
    answer = 987654321
    length = len(s)
    # 1개 이상 절반까지 갯수 표현가능 / 문자열의 두번째 부터 비교 시작한다.
    # 첫번째 값을 가지고 그다음부터 비교함
    for i in range(1, length//2+1):
        check = s[:i]
        tmp = ''
        cnt = 1
        # 인덱스 슬라이싱 개념으로 접근
        for j in range(i, length+i, i):
            if check == s[j:i+j]:
                cnt += 1
            else:
                # 같은 문자열 개수에 따라 정답될 수 있는 tmp 문자열붙인다.
                if cnt != 1:
                    tmp += str(cnt) + check
                else:
                    tmp += check
                # 현재와 다음 문자열이 다를 경우 초기화
                check = s[j:i+j]
                cnt = 1
        if answer > len(tmp):
            answer = len(tmp)
    # 길이가 1인 경우 (문자가 1개만 주어진 경우) 최소 1 임
    if answer == 987654321:
        answer = 1
    return answer
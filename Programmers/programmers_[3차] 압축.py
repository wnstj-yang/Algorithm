def solution(msg):
    answer = []
    idx = 65  # 대문자 아스키코드'A'
    alpha = [0] * 27
    # 문제 인덱스번호에 맞게 각 1~27값에 알파벳 A~Z초기화
    for i in range(1, 27):
        alpha[i] = chr(idx)
        idx += 1
    # start, end의 변수로 인덱스 슬라이싱을 통해
    # 문자 존재 유무 확인
    s, e = 0, 1
    # 시작점인 s부터 시작하여 끝까지의 길이만큼 문자열이 사전에 있는지 체크하면서 반복 진행
    while s < len(msg):
        # 범위를 총 길이에 + 1을 해주어야 문자열 끝까지 슬라이싱이 가능하다
        for i in range(e, len(msg) + 1):
            # 길이만큼 사전에 존재하는지 확인하고 존재하면 문자열 끝 범위 초기화9(e)
            if msg[s:i] in alpha:
                e = i
        # 사전 추가(w+c) 부분에서 인덱스 에러 발생
        # 기존 : temp = msg[s:e] + msg[e]
        # 수정 : temp = msg[s:e+1]
        # 인덱스 슬라이싱 시 e+1 부분이 총 길이를 넘어가도 끝까지를 바라보기 때문에 에러 X
        temp = msg[s:e + 1]
        alpha.append(temp)
        answer.append(alpha.index(msg[s:e]))
        # 끝점이 시작점이 되고, 끝점은 시작점 + 1
        s, e = e, e + 1

    return answer
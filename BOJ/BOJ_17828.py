# Baekjoon Online Judge - 17828번. 문자열 화폐


N, X = map(int, input().split())
result = [65] * N
X -= N
# 그리디하게 N크기만큼의 A문자열을 깔아놓은 상태에서 X 가치를 0으로 만들기 위해 큰 값부터 지워준다
# 다 끝났는데도 0이 아닌 경우에는 X가치를 정확히 만들 수 없으므로 !를 출력
if X < 0:
    print('!')
else:
    for i in range(N):
        if X >= 25:
            result[i] += 25
            X -= 25
        else:
            result[i] += X
            X = 0
            break
    if X:
        print('!')
    else:
        # 아스키코드를 가리켰던 result의 원소들에 각각 문자열로 바꿔준다
        for i in range(N):
            result[i] = chr(result[i])
        # 맨 끝에서부터 진행하므로 뒤바꿔준 이후에 문자열로 출력
        result = result[::-1]
        print(''.join(result))

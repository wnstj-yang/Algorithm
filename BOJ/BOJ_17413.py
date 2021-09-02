# Baekjoon Online Judge - 17413번. 단어 뒤집기2
# [::-1]은 모든 인덱스를 거꾸로 뒤집는다. [1:3:-1]은 1번 인덱스부터 2까지 역으로
S = input()

length = len(S)
ans = ''
idx = 0
temp = ''
# 인덱스를 통해 입력 문자열길이만큼 왔으면 끝
while idx != length:
    # '<>' 안의 문자열은 그대로 넣어준다
    if S[idx] == '<':
        # 이전에 temp안의 문자열이 있다면 즉, <>abc<>이런 경우 역으로 더해주고 다음 진행
        if temp != '':
            ans += temp[::-1]
        temp = ''
        # 안의 값들은 인덱스를 늘려가면서 그대로 넣어준다
        while S[idx] != '>':
            temp += S[idx]
            idx += 1
        # 마지막 까지 왔으면 '>' ans에 넣어주고 temp 초기화
        temp += S[idx]
        idx += 1
        ans += temp
        temp = ''
        continue
    # 공백이 존재하면 하나의 문자열이 끝났다는 의미
    if S[idx] == ' ':
        ans += temp[::-1]
        ans += ' '
        idx += 1
        temp = ''
        continue
    # 위의 두 조건을 제외하면 하나의 문자열을 인덱스 증가하면서 temp에 추가한다.
    temp += S[idx]
    idx += 1

# 마지막 문자열 안에 <>이 존재하면 그대로 넣어주고 아니면 역으로 해서 넣어준다
if '<' in temp:
    ans += temp
else:
    ans += temp[::-1]
print(ans)

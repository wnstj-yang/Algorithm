def solution(s):
    answer = []
    alphabets = {} # 각 문자열의 알파벳들의 인덱스를 나타낸다. 갱신함
    for i in range(len(s)):
        if s[i] not in alphabets: # 알파벳 목록에 알파벳이 없다면
            answer.append(-1) # 처음으로 나온 것이기 때문에 -1을 추가
            alphabets[s[i]] = i # 현재 위치의 인덱스를 초기화 해준다
        else:
            # 알파벳이 존재하면 현재 위치에서 가장 가깝다고 갱신된 알파벳의 인덱스를 빼준다
            answer.append(i - alphabets[s[i]])
            alphabets[s[i]] = i # 현재 위치를 이후에 나올 같은 알파벳이 있는 경우를 대비해 갱신
    return answer

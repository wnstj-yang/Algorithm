def solution(keymap, targets):
    steps = {}  # key안에 있는 문자들을 모아서 거리를 넣는 딕셔너리
    answer = []
    for keys in keymap:
        for i in range(len(keys)):
            # 현재 키안의 문자가 steps안에 없다면 거리를 i + 1값으로 할당(+1하는 이유는 인덱스이기 때문)
            if keys[i] not in steps:
                steps[keys[i]] = i + 1
            else:
                # 거리가 존재한다면 현재 키 안의 문자와의 거리 중 최소 값을 저장한다.
                steps[keys[i]] = min(i + 1, steps[keys[i]])
    # 목표 문자열을 반복문으로 순회
    for target in targets:
        cnt = 0  # 거리의 합을 구하는 cnt
        for t in target:
            if t not in steps:
                answer.append(-1)  # 목표 문자열을 만들 수 없기 때문에 -1을 추가
                cnt = -1  # 만들 수 없음을 표현하기 위해 -1로 초기화
                break
            else:
                cnt += steps[t]
        if cnt != -1:
            answer.append(cnt)

    return answer

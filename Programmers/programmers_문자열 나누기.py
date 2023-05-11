def solution(s):
    answer = 0
    same, diff = 1, 0  # 같은 것과 다른 것의 개수
    idx = 1  # 움직이는 인덱스
    x = s[0]  # s의 첫 글자
    while True:
        # 인덱스가 길이보다 크거나 같다면 끝
        if idx >= len(s):
            break
        if same == diff:  # 문자가 같은 것과 다른 것의 개수가 같다면
            s = s[idx:]  # 문자열을 분리해야하므로 현재 idx부터 끝까지 분리 진행
            answer += 1  # 분리된 문자열 개수 증가
            # 분리가 된 문자열의 길이가 1보다 작거나 같으면 끝
            if len(s) <= 1:
                break
            # 문자열 s가 분리되었으므로 개수, 첫 글자, idx 모두 초기화
            same, diff = 1, 0
            x = s[0]
            idx = 1

        if x == s[idx]:  # 첫 글자가 현재 움직이고 있는 인덱스의 글자와 같다면
            same += 1  # 같다는 개수 증가
        else:
            diff += 1  # 다르다면 다르다는 개수 증가
        idx += 1  # 인덱스 증가로 왼쪽에서 오른쪽으로 이동
    # 현재 분리된 s의 길이가 남아있다면 마지막으로 나머지 문자열을 분리해야 되므로 분해한 문자열 개수 증가
    if s:
        answer += 1

    return answer

def solution(new_id):
    answer = ''
    # 1단계 : 대문자 -> 소문자
    new_id = new_id.lower()
    # 2단계 : 소문자, 숫자, 빼기, 밑줄, 마침표 제외 제거
    temp_id = ''
    for i in new_id:
        if 97 <= ord(i) <= 122 or i == '-' or i == '_' or i == '.' or i.isdecimal():
            temp_id += i
    new_id = temp_id
    # 3단계 마침표가 2번 이상 연속된 부분을 하나로 치환
    cnt = 0  # '.'의 개수
    temp_id = ''
    for i in new_id:
        # 마침표이면 개수 카운트
        if i == '.':
            # 2개 이상인 경우에는 미리 마침표를 넣어주고 카운트
            # 실제로 2개 이상인 경우 넘어간다 ( 미리 마침표를 넣어서 추가로 안함 )
            if cnt == 0:
                temp_id += i
                cnt += 1
        # 마침표 이외의 경우 마침표 카운트를 0으로 초기화 및 문자열 추가
        else:
            temp_id += i
            cnt = 0

    new_id = temp_id
    # 4단계 : 마침표가 처음이나 끝에 위치하면 제거
    new_id = list(new_id)
    if new_id[0] == '.':
        new_id.pop(0)
    elif new_id[-1] == '.':
        new_id.pop()

    # 5단계 : 빈 무자열이면 a를 대입
    if len(new_id) == 0:
        new_id.append('a')

    # 6단계 : 길이가 16 이상이면 첫 15개까지 문자만 살린다
    if len(new_id) >= 16:
        new_id = new_id[:15]

    # 제거 후 마침표가 끝에 있으면 마침표 제거
    if new_id[-1] == '.':
        new_id.pop()

    # 7단계 : 길이가 2이하면 마지막 문자를 더해 길이가 3이 될 때까지 반복해서 끝에 붙인다.
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[-1])

    return ''.join(new_id)
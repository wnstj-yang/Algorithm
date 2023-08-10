def solution(ingredient):
    answer = 0
    target = []  # stack처럼 재료를 쌓는다
    for i in ingredient:
        target.append(i)  # 재료 추가
        # 끝에서부터 4개가 [1, 2, 3, 1] 즉, 빵-야채-고기-빵 으로 쌓였는지 리스트슬라이싱으로 확인
        if target[-4:] == [1, 2, 3, 1]:
            answer += 1
            # 하나의 햄버거가 만들어졌기 때문에 4개의 재료를 지운다
            for _ in range(4):
                target.pop()

    return answer

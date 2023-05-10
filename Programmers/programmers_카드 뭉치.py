def solution(cards1, cards2, goal):
    answer = 'Yes'
    target = [] # goal과 같은지 확인하는 target 리스트
    c1_idx, c2_idx = 0, 0 # cards1과 cards2의 각 인덱스
    for word in goal:
        # cards1의 인덱스가 범위를 벗어나지 않고 현재 단어가 cards1에 있으면 추가해준다
        if c1_idx < len(cards1) and word == cards1[c1_idx]:
            c1_idx += 1
            target.append(word)
        # cards2의 인덱스가 범위를 벗어나지 않고 현재 단어가 cards2에 있으면 추가해준다
        elif c2_idx < len(cards2) and word == cards2[c2_idx]:
            c2_idx += 1
            target.append(word)
        # 그 이외의 경우는 맞지 않으므로 끝낸다.
        else:
            break
    # goal과 똑같지 않은 경우 성립하지 않는다
    if goal != target:
        answer = 'No'
    return answer

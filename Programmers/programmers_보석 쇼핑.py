def solution(gems):
    answer = []
    gem_category = set(gems)
    gem_state = {}
    length = len(gem_category)
    start, end = 0, 0
    dist = len(gems) # 초기 거리설정
    # 투 포인터 활용 거리 측정
    # 1. 거리를 증가하면서 끝점을 1증가 시킨다. (모든 보석이 각각 모여질 때까지)
    while end < len(gems):
        # 존재하지 않는 보석이 있는지 체크하고 있다면 증가
        if gems[end] not in gem_state:
            gem_state[gems[end]] = 1
        else:
            gem_state[gems[end]] += 1
        end += 1
        # 2. 모든 보석이 모아지면 최소 거리를 찾기 위해 시작점을 줄여나가면서 보석의 수를 줄인다.
        if len(gem_state) == length:
            while len(gem_state) == length:
                gem_state[gems[start]] -= 1
                # 줄여 나가면서 보석이 0개가 되면 그 보석을 없앤다.
                if gem_state[gems[start]] == 0:
                    gem_state.pop(gems[start])
                start += 1
                if dist > end - start:
                    dist = end - start
                    answer = [start, end]

    return answer

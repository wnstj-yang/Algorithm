def solution(n, stations, w):
    answer = 0
    start = 1
    idx = 0
    while start <= n:
        # 전파가 닿지 않는 경우
        if idx >= len(stations) or start < stations[idx] - w:
            # 전파 범위 포함 그 다음 위치를 의미하는 1을 더해준다
            start = start + 2 * w + 1
            answer += 1
        # 전파가 닿는 경우 해당 기지국에서부터 w 전파만큼과 다음 위치 의미하는 1을 더해준다
        # 기지국 인덱스는 증가
        else:
            start = stations[idx] + w + 1
            idx += 1

    return answer


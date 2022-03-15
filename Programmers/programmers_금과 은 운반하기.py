def solution(a, b, g, s, w, t):
    answer = -1
    start = 0
    # 옮겨야 할 금,은 양 => 2 * 10^9 / 한번에 옮길 수 있는 양 => 1 / 걸리는 시간 2 * 10^5 (왕복)
    end = 4 * int(1e9) * int(1e5)
    # 이분탐색으로 최적 시간을 찾는다
    answer = end
    while start <= end:
        mid = (start + end) // 2
        gold, silver, total = 0, 0, 0
        for i in range(len(g)):
            time = t[i]
            round_time = time * 2  # 왕복
            cnt = mid // round_time  # 시간 만큼 옮길 수 있는 총 횟수
            # 즉, 운반횟수를 늘릴지 판단(편도이므로 이를 기준삼는다)
            if mid % round_time >= time:
                cnt += 1
            # 보유량과 왕복으로 옮기는 총량 중 최소값
            gold += min(g[i], w[i] * cnt)
            silver += min(s[i], w[i] * cnt)
            total += min(g[i] + s[i], w[i] * cnt)  # 총량
        # 총량을 통해서도 옮길 수 있는 광물 총합과 신도시 건설 시 필요한 총합과 안맞을 수 있기 때문에 필요함
        # 각 기준보다 크면 시간을 줄이고
        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        # 작으면 시간을 늘린다.
        else:
            start = mid + 1

    return answer

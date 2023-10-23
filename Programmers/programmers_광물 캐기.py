def solution(picks, minerals):
    answer = 0
    minerals = minerals[:sum(picks) * 5]
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    costs = []
    for mineral in minerals:
        cost = [0, 0, 0] # 다이아몬드, 철, 돌 곡괭이순으로 광물에 따라 소요되는 비용 카운트 (5개중에)
        for val in mineral:
            if val == 'diamond':
                cost[0] += 1
                cost[1] += 5
                cost[2] += 25
            elif val == 'iron':
                cost[0] += 1
                cost[1] += 1
                cost[2] += 5
            else:
                cost[0] += 1
                cost[1] += 1
                cost[2] += 1
        costs.append(cost)
    costs.sort(key=lambda x:(-x[2], -x[1] ,x[0])) # 돌 곡괭이, 철, 다이아몬드 순으로 내림차순 정렬
    # 여기서 내림차순 정렬을 하는 이유는 광물이 순서대로 가야한다는 문제의 조건에서 헷갈릴 수는 있다.
    # 하지만, 반대로 생각해서 광물 비용부터 구하고 어디에 곡괭이를 위치 시키는 지가 중점이므로 거꾸로 생각하면 된다.
    for cost in costs:
        # 각 곡괭이별로 사용되는 광물의 비용을 값이 큰 순서대로 정렬했으므로
        # 비용이 적게드는 곡괭이 순서로 해서 빼준다
        if picks[0] > 0:
            picks[0] -= 1
            answer += cost[0]
        elif picks[1] > 0:
            picks[1] -= 1
            answer += cost[1]
        elif picks[2] > 0:
            picks[2] -= 1
            answer += cost[2]
    return answer

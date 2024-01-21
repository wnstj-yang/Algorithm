import heapq


def solution(n, k, enemy):
    answer = 0
    q = []
    _sum = 0 # 무적권 막아내면서 나타내는 적의 수 / sum 내장함수 사용 시 시간초과 발생
    for i in range(len(enemy)):
        heapq.heappush(q, -enemy[i])
        _sum += enemy[i] # 공격해오는 적의 수 증가
        # 공격하는 적의 수 합 > 막아낼 수 있는 수
        if _sum > n:
            if k: # 무적권 방어 가능 횟수
                k -= 1
                _sum += heapq.heappop(q) # 가장 큰 수를 빼준다.
            else:
                break
        answer += 1
    return answer

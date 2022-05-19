import heapq


def solution(n, works):
    # 시간 내에 모두 작업을 해결할 수 있는 경우 피로도가 0
    if sum(works) <= n:
        return 0

    answer = 0
    # 최대힙으로 바꾸기위해 앞에 -를 적용(heapq 모듈이 최소힙이기 때문)
    works = [-i for i in works]
    heapq.heapify(works) # 힙으로 만들어줌
    for _ in range(n):
        # 최대 값인 작업들로부터 1씩 줄여나간다.( = 1을 더함)
        num = heapq.heappop(works)
        heapq.heappush(works, num + 1)

    for num in works:
        answer += (num ** 2)
    return answer

import heapq

def solution(scoville, K):
    answer = -1
    cnt = 0
    heapq.heapify(scoville)
    # heapq로 맨앞이 최소값이므로 K이상인지 판단
    while scoville[0] < K:
        num = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, num)
        # 숫자가 1개가 남으면 마지막 체크, K이상이 될 수 없으니 cnt를 0으로 줘서 -1 return하게한다.
        if len(scoville) == 1 and scoville[0] < K:
            cnt = 0
            break
        cnt += 1
    if cnt != 0:
        answer = cnt
    return answer
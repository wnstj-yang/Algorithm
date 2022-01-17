import heapq

def solution(operations):
    answer = []
    # 최소, 최대 힙을 각각 구해서 진행
    min_q = []
    max_q = []
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            heapq.heappush(min_q, int(operations[i][2:]))
            # 최대 힙의 경우 튜플로 우선순위를 마이너스값을 통해 진행
            heapq.heappush(max_q, (-int(operations[i][2:]), int(operations[i][2:])))
        else:
            # 비어있지 않을 때 (같이 진행되므로 하나만 해도 된다)
            if len(min_q) != 0:
                if operations[i][2] == '1': # 정수가 아닌 문자열..
                    # 최댓값 삭제(최소값에도 최댓값을 삭제해주어야한다)
                    max_val = heapq.heappop(max_q)
                    min_q.remove(max_val[1])
                else:
                    # 최솟값 삭제(최댓값에도 최소값을 삭제해주어햐한다)
                    min_val = heapq.heappop(min_q)
                    max_q.remove((-min_val, min_val))
    # 비어있다면 [0, 0]
    if len(min_q) == 0:
        answer = [0, 0]
    # 비어있지 않다면 최대힙에서의 최대값, 최소힙에서의 최소값을 반환
    else:
        answer = [heapq.heappop(max_q)[1], heapq.heappop(min_q)]
    return answer
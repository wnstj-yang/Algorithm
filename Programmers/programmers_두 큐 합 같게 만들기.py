from collections import deque


def solution(queue1, queue2):
    answer = -1
    target = (sum(queue1) + sum(queue2)) // 2
    queue1, queue2 = deque(queue1), deque(queue2)
    queue1_sum, queue2_sum = sum(queue1), sum(queue2)
    check = False
    cnt = 0
    # 연산 도중 총 합의 절반이 되지 않는 경우가 생길 때 무한루프가 생기므로 제한을 둬야한다
    # 3으로 설정한 이유는 1번 큐의 원소들이 2번 큐의 원소들로 갔다가
    # 다시 2번 큐의 원소들이 1번큐로 돌아오는 과정들을 봤을 때
    # n번 갔다 최대 2n번의 경우를 생각하여 총 3n 횟수로 설정
    for _ in range(len(queue1) * 3):
        if queue1_sum > target:
            queue2_sum += queue1[0]
            queue1_sum -= queue1[0]
            queue2.append(queue1.popleft())

        elif queue1_sum < target:
            queue1_sum += queue2[0]
            queue2_sum -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            check = True
            break
        cnt += 1
    if check:
        answer = cnt

    return answer


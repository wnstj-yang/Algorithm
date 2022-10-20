# 두 포인터 활용


def solution(queue1, queue2):
    answer = -1
    target = (sum(queue1) + sum(queue2)) // 2
    queue = queue1 + queue2
    base = sum(queue1)
    l, r = 0, len(queue1)
    cnt = 0
    # 2n길이의 합쳐진 큐를 2번 곱한 만큼 횟수를 돌린다
    # 한쪽으로 갔다가 다시 다른 한쪽으로 옮겨지고 교차하는것까지 4n
    while cnt < len(queue) * 2:
        # 두 포인터를 활용해서 인덱스 위치 변경
        if base < target:
            base += queue[r]
            r += 1
            r = r % len(queue)
        elif base > target:
            base -= queue[l]
            l += 1
            l = l % len(queue)
        else:
            answer = cnt
            break
        cnt += 1
    if base == target:
        answer = cnt

    return answer


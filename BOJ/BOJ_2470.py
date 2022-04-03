# Baekjoon Online Judge - 2470번. 두 용액

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
start, end = 0, N - 1
# 혼동 방지 위해 절댓값으로 0과 가까운지 판단 + 초기설정
close_to_zero = abs(liquids[start] + liquids[end])
answer = [0] * 2
answer[0], answer[1] = liquids[start], liquids[end]
# 서로 다른 용액이므로 탐색 시 같은 것은 방지(범위 설정)
while start < end:
    # 둘의 합을 구한다
    temp_sum = liquids[start] + liquids[end]
    # 0과 가까운 판단은 절댓값으로
    if close_to_zero > abs(temp_sum):
        # start, end는 각각 정렬된 상태에서의 인덱스이기 때문에
        answer[0], answer[1] = liquids[start], liquids[end]
        close_to_zero = abs(temp_sum)
    # 합이 0보다 작으면 플러스쪽으로 옮겨야 하므로 start(왼쪽)인덱스 증가
    if temp_sum < 0:
        start += 1
    # 합이 0 보다 크거나 같으면 마이너스 쪽으로 옮겨야 하므로 end(오른쪽)인덱스 감소
    else:
        end -= 1
print(*answer)

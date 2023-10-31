# Baekjoon Online Judge - 7795번. 먹을 것인가 먹힐 것인가

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    total = 0
    A.sort()
    B.sort()
    for i in A:
        left, right = 0, len(B) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            # A는 자기보다 크기가 작은 먹이만 먹을 수 있음
            if i > B[mid]:
                left = mid + 1
                index = mid
            else:
                right = mid - 1
        # index까지 먹을 수 있으므로 감당 가능한 index까지의 수를 구한다.
        # 없는 경우 아래의 1을 추가적으로 항상 더해주기 때문에 0으로 마무리한다.
        # index를 0으로 하면 개수로 인식하지 못하여 1을 추가함
        total += (index + 1)
    print(total)
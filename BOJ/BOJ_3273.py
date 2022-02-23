# Baekjoon Online Judge - 3273번. 두 수의 합

N = int(input())
numbers = list(map(int, input().split()))
X = int(input())
numbers.sort() # 투 포인터 활용을 위해 정렬
left, right = 0, N - 1 # 맨 앞과 끝에서부터 두 수의 합을 구한다.
answer = 0
while left < right:
    # 두 쌍의 합 
    result = numbers[left] + numbers[right]
    # X의 합을 구하면 개수 + 1을 진행 후 left를 증가시킨다.
    if result == X:
        answer += 1
        left += 1
    # X보다 작다면 합이 적으므로 left 증가
    elif result < X:
        left += 1
    # X보다 크다면 합이 작아야되므로 right 감소
    else:
        right -= 1
print(answer)


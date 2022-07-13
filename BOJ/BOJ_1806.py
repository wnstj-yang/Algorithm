# Baekjoon Online Judge - 1806번. 부분합

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, 0 # 투 포인터를 활용해서 그 합의 길이를 체크
result = numbers[left] # 첫 번째 값을 넣고 시작
min_length = 987654321
while True:
    # 현재 길이만큼의 합이 S보다 크거나 같을 때
    if result >= S:
        min_length = min(min_length, right - left + 1) # 인덱스 상에서 길이를 빼고 + 1 진행
        result -= numbers[left] # 최소 길이를 구해야하므로 길이 1을 줄인다. 그래서 현재의 left값을 빼줌
        left += 1
    # S보다 작을 때
    else:
        # right 값을 증가시키면서 값을 늘린다. S보다 크거나 같기 위해서
        right += 1
        if right == N:
            break
        result += numbers[right]
# 최소 길이를 구할 수 없는 경우에는 0 아니면 길이 출력
if min_length == 987654321:
    print(0)
else:
    print(min_length)

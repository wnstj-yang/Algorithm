# Baekjoon Online Judge - 2110번. 공유기 설치

N, C = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))
homes.sort()
result = 0
start = 0
end = homes[-1] # 맨 마지막의 값으로 이분탐색 진행
while start <= end:
    mid = (start + end) // 2
    current = homes[0]
    cnt = 1 # 정렬 후 맨 처음 값을 가지므로 애초에 스타트가 개수 1개임
    for i in range(1, len(homes)):
        # 현재의 집 + 기준 거리 <= 다음 집 까지의 거리를 통해 와이파이 연결이 가능한지 파악한다.
        # 조건에 맞다면 설치 가능하므로 개수를 늘린다.
        if current + mid <= homes[i]:
            cnt += 1
            current = homes[i]
    # 개수가 같거나 크다면 기준 거리를 크게 한다.
    if cnt >= C:
        result = mid
        start = mid + 1
    # 개수가 작다면 기준 거리를 작게 한다.
    else:
        end = mid - 1
print(result)

# Baekjoon Online Judge - 1477번. 휴게소 세우기

N, M, L = map(int, input().split())
rest_areas = [0] + list(map(int, input().split())) + [L]
rest_areas.sort()
result = 0
left, right = 1, L - 1 # 조건에서 1 <= 휴게소의 위치 <= L - 1표현
# 휴게소가 없는 구간의 최댓값을 휴게소를 설치하여 최소로 만들어간다.
# 즉, mid보다 큰 구간이 있으면 휴게소 mid만큼 나눈 몫(휴게소의 개수)에 따라 최소가 될 수 있는지와 없는지 판단한다.
while left <= right:
    mid = (left + right) // 2 # 최소 거리를 찾아가는 과정
    cnt = 0
    for i in range(1, len(rest_areas)):
        if rest_areas[i] - rest_areas[i - 1] > mid:
            cnt += (rest_areas[i] - rest_areas[i - 1] - 1) // mid # 1을 빼주는 이유는 같은 자리에 휴게소 설치가 불가능 하기 때문
            
    # 휴게소 설치 개수가 M보다 많으면 줄여야 하므로 left 증가
    if cnt > M:
        left = mid + 1
    # 휴게소 설치 개수가 M보다 작거나 같다면 늘려준다
    else:
        right = mid - 1
        result = mid
print(result)



# Baekjoon Online Judge - 2805번. 나무 자르기

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)
max_height = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0 # 절단한 나무의 개수(길이)
    for tree in trees:
        if tree >= mid:
            cnt += (tree - mid)
    # 정확하게 M인 경우에 구하는 것이 아니라(더 최대가 있을 수 있기 때문) 이분 탐색을 끝까지 진행
    # 그래서 '적어도' M미터 이상 중 최댓값을 구하는 것이다.
    # 절단한 나무의 길이가 M미터 이상일 때 많이 잘라진 경우라고 생각해서 높이를 높인다.(덜 잘리게)
    if cnt >= M:
        max_height = mid
        start = mid + 1
    # 절단한 나무의 길이가 M미터보다 작다면 높이를 줄여서 많이 잘라지게 한다.
    else:
        end = mid - 1
print(max_height)

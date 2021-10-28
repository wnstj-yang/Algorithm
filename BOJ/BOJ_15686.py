# Baekjoon Online Judge - 15686번. 치킨 배달
# 최대 M까지 구하는 것인줄 알았으나 치킨집이 많을수록 치킨 거리가 짧아지므로 M크기의 조합만 구하면된다!!!!
# 각 집에서 가까운 치킨집을 선택하기 때문

def check(k, idx):
    global result
    if k == M:
        cnt = 0
        for j in range(h_length):
            h_x, h_y = home_list[j]
            tmp = 0
            min_num = 9876542321
            for n in range(k):
                s_x, s_y = ans_list[n]
                tmp = abs(h_x - s_x) + abs(h_y - s_y)
                if min_num > tmp:
                    min_num = tmp
            cnt += min_num
            # 중간에 결과보다 크다면 끝
            if cnt > result:
                return
        if result > cnt:
            result = cnt
        return
    # idx 시작점을 조합으로 주어서 시간 줄여야함
    for i in range(idx, s_length):
        if not visited[i]:
            visited[i] = True
            ans_list[k] = stores[i]
            # idx+1로 해놔서 시간초과 발생, i값 넣어야 조합
            check(k+1, i+1)
            visited[i] = False


N, M = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(N)]

# 1. 최대 M까지의 치킨집의 수 => 조합을 구해야함 => M만 구해도 된다.
# 2. 집의 위치를 구한 곳에서 조합을 통해 구한 치킨집의 수와 위치에 대한 거리값 계산
# 3. 조합의 경우의 수에서 거리 값의 최소 값을 구한다

# 치킨 집들, 집들
stores = []
home_list = []
for i in range(N):
    for j in range(N):
        if city_info[i][j] == 2:
            stores.append((i, j))
        if city_info[i][j] == 1:
            home_list.append((i, j))
result = 987654321
visited = [False] * len(stores)
h_length, s_length = len(home_list), len(stores)
# 최대 M까지 => M만
ans_list = [0] * M
check(0, 0)
print(result)

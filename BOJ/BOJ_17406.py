# Baekjoon Online Judge - 17406번. 배열 돌리기 4

def dfs(idx):
    global K
    if idx == K:
        seq.append(list(ans))
        return
    for i in range(len(ans)):
        if not visited[i]:
            visited[i] = True
            ans[idx] = i
            dfs(idx+1)
            visited[i] = False


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 좌표 범위 담는 리스트
coor = []
# 순열로 만들어진 순서 리스트
seq = []
for _ in range(K):
    r, c, s = map(int, input().split())
    coor.append((r, c, s))
# 방문 체크 및 순서 담는 ans
visited = [False] * len(coor)
ans = [0] * len(coor)
dfs(0)
# 최소 값
result = 987654321
# dfs를 통해 순열로 가져온 순서를 구한다
for i in range(len(seq)):
    temp_arr = [item[:] for item in arr]
    # 주어진 순서대로 진행
    for j in range(len(seq[i])):
        r, c, s = coor[seq[i].index(j)]
        r, c = r - 1, c - 1
        for k in range(s, 0, -1):
            # 좌 -> 우의 끝에 있는 값을 저장
            first = temp_arr[r-k][c+k]
            # 좌 -> 우
            temp_arr[r-k][c-k+1:c+k+1] = temp_arr[r-k][c-k:c+k]
            # 하 -> 상
            for z in range(r-k, r+k):
                temp_arr[z][c-k] = temp_arr[z+1][c-k]
            # 우 -> 좌
            temp_arr[r+k][c-k:c+k] = temp_arr[r+k][c-k+1:c+k+1]
            # 상 -> 하
            for z in range(r+k, r-k, -1):
                temp_arr[z][c+k] = temp_arr[z-1][c+k]
            temp_arr[r-k+1][c+k] = first

    for item in temp_arr:
        result = min(result, sum(item))

print(result)



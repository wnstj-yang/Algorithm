def dfs(visited, N, k, cnt, dungeons):
    global answer
    answer = max(answer, cnt)
    for i in range(N):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(visited, N, k - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = False


def solution(k, dungeons):
    global answer
    answer = 0
    visited = [False] * len(dungeons)
    dfs(visited, len(dungeons), k, 0, dungeons)
    return answer

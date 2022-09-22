# Baekjoon Online Judge - 15661번. 링크와 스타트


def combi(idx, cnt, k):
    if cnt == k:
        comb_list.append(list(temp))
        return

    for j in range(idx, N):
        if not visited[j]:
            visited[j] = True
            temp[cnt] = standard[j]
            combi(j, cnt + 1, k)
            visited[j] = False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
standard = list(range(N))
result = 987654321

# 절반까지의 수만큼 조합을 구한다.
for i in range(1, N // 2 + 1):
    comb_list = []
    temp = [0] * i
    visited = [False] * N
    combi(0, 0, i)

    for c in range(len(comb_list)):
        start, link = 0, 0
        v_nums = [1] * N
        for j in comb_list[c]:
            v_nums[j] -= 1
        # 나온 조합을 바탕으로 N만큼 수를 방문표시 한 것과 안한 것으로 각각 더해주는 과정을 거친다.
        for x in range(N):
            for y in range(N):
                if v_nums[x] and v_nums[y]:
                    start += arr[x][y]
                elif not v_nums[x] and not v_nums[y]:
                    link += arr[x][y]
        result = min(result, abs(start - link))

print(result)

# Baekjoon Online Judge - 1967번. 트리의 지름


def postorder(n, node, cnt):
    global ans, check
    if n != 0:
        postorder(child[n][0], node, cnt + weight[n][0])
        if n == node:
            check = True
        postorder(child[n][1], node, cnt + weight[n][1])
        if check == False:
            if cnt not in get_ans:
                get_ans.append(cnt)
    else:
        if check:
            for i in get_ans:
                temp = i + cnt
                if temp > ans:
                    ans = temp
        else:
            if cnt not in get_ans:
                get_ans.append(cnt)


n = int(input())
child = [[0] * 2 for _ in range(n+1)]
weight = [[0] * 2 for _ in range(n+1)]
ans = 0
for i in range(n-1):
    x, y, z = map(int, input().split())
    if child[x][0] == 0:
        child[x][0] = y
        weight[x][0] = z
    elif child[x][1] == 0:
        child[x][1] = y
        weight[x][1] = z


for i in range(1, n+1):
    get_ans = []
    check = False
    postorder(i, i, 0)
    print(get_ans)


print(ans)
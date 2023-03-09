# DFS/BFS - 유형별. 연산자 끼워 넣기 349p

def dfs(k, num):
    global max_num, min_num
    if k == N:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    for i in range(4):
        if operations[i] > 0:
            operations[i] -= 1
            if i == 0:
                dfs(k + 1, num + numbers[k])
            elif i == 1:
                dfs(k + 1, num - numbers[k])
            elif i == 2:
                dfs(k + 1, num * numbers[k])
            else:
                if num < 0:
                    num = -num
                    num = -(num // numbers[k])
                else:
                    num = num // numbers[k]
                dfs(k + 1, num)
            operations[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))
max_num = -int(1e9)
min_num = int(1e9)
dfs(1, numbers[0])
print(max_num)
print(min_num)

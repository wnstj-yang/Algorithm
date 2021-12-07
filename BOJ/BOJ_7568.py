# Baekjoon Online Judge - 7568번. 덩치

N = int(input())
info = []
for _ in range(N):
    x, y = map(int, input().split())
    info.append((x, y))

for i in range(N):
    rank = 1
    # 나보다 큰 사람이 몇명인지 체크하면 등수를 알 수 있다.
    for j in range(N):
        if i != j and info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            rank += 1
    print(rank, end=' ')

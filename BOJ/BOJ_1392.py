# Baekjoon Online Judge - 1392번. 노래 악보

N, Q = map(int, input().split())
musics = []

# 입력받은 시간을 각 1번 악보부터 지속되는 시간을 저장
for time in range(1, N + 1):
    M = int(input())
    for _ in range(M):
        musics.append(time)

for _ in range(Q):
    q = int(input())
    print(musics[q])

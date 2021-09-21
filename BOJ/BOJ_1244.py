# Baekjoon Online Judge - 1244번. 스위치 켜고 끄기
# 문제를 잘 읽어야함


# toggle
def change_num(n):
    if switches[n] == 1:
        switches[n] = 0
    else:
        switches[n] = 1


N = int(input())
switches = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    sex, pos = map(int, input().split())
    if sex == 1:
        # 아래처럼 따로 지정하지 않은 경우
        num = pos
        while pos-1 < N:
            change_num(pos-1)
            pos += num
    else:
        # 현재 위치 toggle
        change_num(pos-1)
        # 현재 위치 기준 왼쪽 s, 오른쪽 e 에서 각각 -1, 1씩 인덱스 변화
        s, e = pos - 2, pos
        # 각 인덱스들을 다 구해서 toggle할 때 사용
        change = []
        while True:
            # 인덱스 범위에서 벗어날 때
            if s < 0 or e >= len(switches):
                break
            # 양쪽이 다르다면 끝
            if switches[s] != switches[e]:
                break
            else:
                change.append((s, e))
                s -= 1
                e += 1
        # 구한 인덱스들을 toggle한다
        while change:
            s, e = change.pop()
            change_num(s)
            change_num(e)
idx = 0
# 각 20개씩 잘라서 출력을 해야한다
while idx < len(switches):
    print(*switches[idx:idx+20])
    idx += 20

# Baekjoon Online Judge - 14890번. 경사로

def check(line):
    visited = [False] * N # 경사로의 중복을 피한다.
    for i in range(N - 1):
        num = abs(line[i] - line[i + 1])
        if num > 1:
            return False
        elif num == 1:
            if line[i] - line[i + 1] == 1: # 내리막길
                for j in range(L):
                    # + 1을 더해주는 이유는 다음 위치에서부터 L길이만큼 같은 수가 오른쪽에 존재할 때 내리막길의 경사로를 만들어야 하기 때문임
                    if i + j + 1 >= N or visited[i + j + 1] or line[i + j + 1] != line[i + 1]:
                        return False
                    elif line[i + 1] == line[i + j + 1]:
                        visited[i + j + 1] = True
            elif line[i] - line[i + 1] == -1: # 오르막길
                # 다음 위치가 값이 더 크기 때문에 현재 위치에서부터 L길이 만큼 같은 수가 왼쪽에 존재할 때 오르막길의 경사로를 만든다.
                for j in range(L):
                    if i - j < 0 or visited[i - j] or line[i] != line[i - j]:
                        return False
                    elif line[i] == line[i - j]:
                        visited[i - j] = True
    return True


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
for row in board: # 행
    if check(row):
        result += 1

for j in range(N): # 열
    temp = []
    for i in range(N):
        temp.append(board[i][j])
    if check(temp):
        result += 1
print(result)


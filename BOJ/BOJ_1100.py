# Baekjoon Online Judge - 1100번. 하얀 칸

chess = []
for _ in range(8):
    chess.append(list(map(str, input())))
result = 0
for i in range(8):
    for j in range(8):
        if i % 2 == j % 2 and chess[i][j] == 'F':
            result += 1
print(result)

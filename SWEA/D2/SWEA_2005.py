# SW Expert Academy - 2005번. 파스칼의 삼각형

T = int(input())

# 파스칼 삼각형을 10줄까지 미리 구해놓는다. 양끝은 1로 만들고, 그 이외는 왼쪽 위 대각선, 오른쪽 위 대각선 더한 값을 넣는다.
arr = [[0] * 11 for _ in range(11)]
for i in range(1, 11):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(arr[i][j], end=' ')
        print()

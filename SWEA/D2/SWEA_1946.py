# SW Expert Academy - 1946번. 간단한 압축 풀기

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = ''
    for _ in range(N):
        alpha, cnt = map(str, input().split())
        result += alpha * int(cnt)
    print('#{}'.format(tc))

    for i in range(0, len(result), 10):
        print(result[i:i+10])

# SW Expert Academy - 14178번. 1차원 정원

T = int(input())

for tc in range(1, T + 1):
    N, D = map(int, input().split())
    D = D * 2 + 1 # 모든 꽃에 물을 줄 수 있는 범위
    result = 0
    result += N // D # 전체 길이에서 나눈 다음 
    N = N % D # 남은 값이 존재하면 하나 더 추가
    if N:
        result += 1
    print('#{} {}'.format(tc, result))

# SW Expert Academy - 4466번. 최대 성적표 만들기


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    print('#{} {}'.format(tc, sum(scores[:K])))

# Baekjoon Online Judge - 5766번. 할아버지는 유명해!

while True:
    N, M = map(int, input().split())
    # 0, 0으로 입력받으면 끝
    if N == 0 and M == 0:
        break

    ranks = {} # 랭킹 정보를 저장하는 딕셔너리. key : 선수 번호 / value : 포인트
    for _ in range(N):
        rank_info = list(map(int, input().split()))
        # 각 선수 번호들을 입력받은 이후 포인트들을 올린다. 없으면 1로 초기화
        for num in rank_info:
            if num not in ranks:
                ranks[num] = 1
            else:
                ranks[num] += 1
    # 점수는 내림차순, 번호는 오름차순으로 정렬 진행
    ranks = sorted(ranks.items(), key=lambda x:(-x[1], x[0]))
    second = ranks[1][1] # 2등 선수의 포인트
    ans = [ranks[1][0]] # 2등 선수의 선수 번호
    # 3번째 선수들부터 2등인지 판단하고 아니라면 끝. 맞다면 선수 번호 추가
    for num, cnt in ranks[2:]:
        if cnt == second:
            ans.append(num)
        else:
            break
    print(*ans)

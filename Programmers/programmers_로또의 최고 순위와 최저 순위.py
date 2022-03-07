def solution(lottos, win_nums):
    answer = [0] * 2
    rank = [6, 6, 5, 4, 3, 2, 1] # 일치 번호 0 or 1개는 6등
    cnt = 0 #
    for num in lottos:
        if num in win_nums:
            cnt += 1
    # 알아볼 수 없는 번호들의 개수(0인 개수)
    zeros = lottos.count(0)
    # 최대, 최소 순위 입력
    answer[0] = rank[cnt + zeros]
    answer[1] = rank[cnt]
    return answer
def solution(genres, plays):
    # 각 장르 별 고유번호와 노래 재생 횟수를  구한다.
    result = {}
    # 각 장르별로 총 노래 재생 횟수의 합
    play_sum = {}
    answer = []
    name = set(genres)
    # 중복되는 genre를 없앤다.
    for i in name:
        result[i] = []
        play_sum[i] = 0
    # 장르로 받은 개수를 돌린다.
    for i in range(len(genres)):
        # 아래의 경우 각 장르별로 고유 번호의 노래와 재생 횟수 저장
        result[genres[i]].append((plays[i], i))

        # play_sum은 각 장르의 노래 재생 횟수의 합을 구한다.
        play_sum[genres[i]] += plays[i]

    # 각각 장르내에서 많이 재생된 노래를 내림차순으로 정렬하고,
    # 같은 노래일 때는 고유번호가 낮은 노래를 먼저 수록하므로 오름차순 정렬
    for i in name:
        result[i].sort(key=lambda x: (x[0], -x[1]), reverse=True)
    # 딕셔너리 key, value로 나누어서 value값을 내림차순으로 정렬
    play_sum = sorted(play_sum.items(), key=lambda x: x[1], reverse=True)
    for genre in play_sum:
        # cnt로 2개씩 구한다.
        cnt = 0
        # genre[0]은 내림차순된 장르
        for item in result[genre[0]]:
            if cnt >= 2:
                break

            answer.append(item[1])
            cnt += 1

    return answer
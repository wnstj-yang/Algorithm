def solution(genres, plays):
    answer = []
    genres_cnt = {}
    genres_list = {}
    for i in range(len(genres)):
        if genres[i] not in genres_cnt:
            genres_cnt[genres[i]] = plays[i]
        else:
            genres_cnt[genres[i]] += plays[i]

        if genres[i] not in genres_list:
            genres_list[genres[i]] = [[plays[i], i]]
        else:
            genres_list[genres[i]].append([plays[i], i])

    genres_cnt = sorted(genres_cnt.items(), key=lambda x: -x[1])

    for genre, val in genres_cnt:
        genres_list[genre].sort(key=lambda x: (-x[0], x[1]))
        if len(genres_list[genre]) >= 2:
            answer.append(genres_list[genre][0][1])
            answer.append(genres_list[genre][1][1])
        else:
            answer.append(genres_list[genre][0][1])

    return answer

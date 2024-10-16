def solution(data, ext, val_ext, sort_by):
    answer = []
    order = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3
    }
    data.sort(key=lambda x: (x[order[ext]]))
    # print(data)
    for d in data:
        if d[order[ext]] < val_ext:
            answer.append(d)
    answer.sort(key=lambda x: (x[order[sort_by]]))
    return answer
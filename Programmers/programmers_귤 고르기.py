# 귤 고르기

def solution(k, tangerine):
    answer = 0
    t_cnt = {}
    for t in tangerine:
        if t not in t_cnt:
            t_cnt[t] = 1
        else:
            t_cnt[t] += 1
    sort_t = sorted(t_cnt.values(), reverse=True)
    for num in sort_t:
        k -= num
        answer += 1
        if k <= 0:
            break
    return answer

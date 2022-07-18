def solution(n, results):
    answer = 0
    wins = [[] for _ in range(n + 1)]
    loses = [[] for _ in range(n + 1)]
    for x, y in results:
        wins[x].append(y)
        loses[y].append(x)

    for i in range(1, n + 1):
        # i가 이긴 선수들
        for w in wins[i]:
            # i한테 진 선수들
            if loses[i]:
                # i가 이긴 선수와 i한테 진 선수가 있을 때
                for l in loses[i]:
                    # 진 선수는 이긴 선수들에 대해 항상 진다.
                    if l not in loses[w]:
                        loses[w].append(l)
                    # 이긴 선수는 진 선수들에 대해 항상 이긴다
                    if w not in wins[l]:
                        wins[l].append(w)

    for i in range(1, n + 1):
        # 순위 판단을 위해서 이기고 진 결과의 합이 n - 1만큼 있어야 판단이 가능하다
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer

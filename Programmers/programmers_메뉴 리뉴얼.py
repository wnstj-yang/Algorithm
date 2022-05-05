def combination(idx, k, cnt, order):
    global result, visited, temp
    if k == cnt:
        result.append(list(temp))
        return
    # 조합 구하기
    for i in range(idx, len(order)):
        if not visited[i]:
            visited[i] = True
            temp[k] = order[i]
            combination(i, k + 1, cnt, order)
            visited[i] = False


def solution(orders, course):
    global result, visited, temp
    answer = []
    # 각 course 요리 개수
    for num in course:
        result = []
        comb_list = {}
        # 각 요리 개수에 따른 order의 조합을 구한다
        for order in orders:
            visited = [False] * len(order)
            temp = [0] * num
            combination(0, 0, num, order)

        for comb in result:
            comb.sort()  # 구해진 조합들을 오름차순으로 정렬
            comb = ''.join(comb)
            if comb not in comb_list:
                comb_list[comb] = 1
            else:
                comb_list[comb] += 1
        # 비어있지 않을 때 각각 내림차순으로 정렬을 진행하고 가장 많이 함께 주문한 조합들이 나온 개수
        if len(comb_list) > 0:
            max_val = max(comb_list.values())
            comb_list = sorted(comb_list.items(), key=lambda x: x[1], reverse=True)
        for i in comb_list:
            # max_val보다 낮다면 해당하는 코스 메뉴의 조합이 아니므로 끝
            if i[1] < max_val:
                break
            else:
                # 해당 조합이 존재해도 최소 2명의 손님이 필요함
                if i[1] >= 2:
                    answer.append(i[0])
        answer.sort()
    return answer


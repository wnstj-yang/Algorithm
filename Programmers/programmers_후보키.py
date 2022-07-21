def combi(k, idx, N, visited, col):
    global result, comb
    if k == N:
        result.append(list(comb))
        return
    for i in range(idx, col):
        if not visited[i]:
            visited[i] = True
            comb[k] = i
            combi(k + 1, i, N, visited, col)
            visited[i] = False


def solution(relation):
    global result, comb

    answer = 0
    row, col = len(relation), len(relation[0])
    uniques = []
    # 조합으로 각각 
    for i in range(1, col + 1):
        result = []
        comb = [0] * i
        visited = [False] * col
        combi(0, 0, i, visited, col)

        for item in result:  # 후보키 조합
            unique_list = []
            # 각 조합에 있는 키들에 릴레이션에 맞춰서 중복이 있는지 없는지 체크한 후에
            # 길이에 맞게 있는 경우 유일성으로 판단해서 해당 키를 넣는다
            for rel in relation:
                temp = []
                for key in item:
                    temp.append(rel[key])
                if temp not in unique_list:
                    unique_list.append(list(temp))
            if len(unique_list) != row:
                continue
            uniques.append(item)

    visited = [1] * len(uniques)
    # 유일성들 중 최소성을 판단할 때 교집합을 진행하여 길이가 같은 경우
    # 현재 키로도 충분히 후보키가 되므로 이후 길이가 더 긴 것들에 대해서 구분을 할 필요가 없어서
    # 0으로 처리
    for i in range(len(uniques)):
        for j in range(i + 1, len(uniques)):
            if len(uniques[i]) == len(set(uniques[i]) & set(uniques[j])):
                visited[j] = 0
    answer = visited.count(1)

    return answer

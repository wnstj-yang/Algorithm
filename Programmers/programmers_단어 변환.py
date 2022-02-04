def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    q = [(begin, 0)]  # 단어와 단계 과정 횟수
    visited = [False] * len(words)
    while q:
        word, num = q.pop()
        # target 찾았다면 끝
        if word == target:
            answer = num
            break
        for i in range(len(words)):
            # 방문하지 않는 단어일 때
            if not visited[i]:
                cnt = 0
                # 조건 1인 한 번에 한개의 알파벳만 바뀌었는지 체크
                for j in range(len(words[i])):
                    if word[j] != words[i][j]:
                        cnt += 1
                # 조건 1에 부합하다면 큐에 단어와 횟수를 넣는다.
                if cnt == 1:
                    visited[i] = True
                    q.append((words[i], num + 1))

    return answer
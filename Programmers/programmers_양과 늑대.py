# 이진 트리 상태, 방문 체크, info(양인지 늑대인지), 양의 수, 늑대의 수
def dfs(state, visited, info, sheep, wolf):
    global answer
    # 양과 늑대가 같다면 되돌아간다
    if sheep == wolf:
        return

    # 최대값을 최신화해준다
    answer = max(answer, sheep)

    # 방문 체크이면서 경로라고 생각하면 편하다
    for i in range(len(visited)):
        if visited[i]:
            for child in state[i]:
                # 자식 노드에서 방문하지 않았다면 체크 후 늑대인지 양인지 판단
                if not visited[child]:
                    visited[child] = True
                    if info[child] == 0:
                        dfs(state, visited, info, sheep + 1, wolf)
                    else:
                        dfs(state, visited, info, sheep, wolf + 1)
                    # 양과 늑대 수가 같다면 되돌린다.
                    visited[child] = False


def solution(info, edges):
    global answer

    answer = 0
    # 이진 트리이기에 자식이 최대 2개임
    state = [[0] * 2 for _ in range(len(info))]
    visited = [False] * len(info)
    # 첫 양은 방문 표시
    visited[0] = True
    for edge in edges:
        if state[edge[0]][0] == 0:
            state[edge[0]][0] = edge[1]
        else:
            state[edge[0]][1] = edge[1]
    # 이진 트리 상태, 방문 체크, info(양인지 늑대인지), 양의 수, 늑대의 수
    dfs(state, visited, info, 1, 0)

    return answer

def solution(board, moves):
    answer = 0
    stack = []
    # 1. 해당 열을 찾으면서 0이 아니라면 그거를 stack으로
    # 2. stack에 넣기 전에 마지막 거랑 같으면 pop함
    # 3. 같지 않으면 stack에 넣는다
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                if len(stack) != 0 and stack[-1] == board[i][move - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move - 1])
                board[i][move - 1] = 0
                break

    return answer

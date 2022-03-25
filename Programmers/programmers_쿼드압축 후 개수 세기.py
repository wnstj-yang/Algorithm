def check_quad(x, y, n, arr):
    global answer
    # 2x2 영역이 만들어질 때 각 수를 카운트
    if n == 1:
        answer[arr[x][y]] += 1
        return

    check = False  # 한 영역에 같은지 다른지 판단
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                check = True
                break
        if check:
            break
    # 다를 때 분할을 더 함 
    if check:
        check_quad(x, y, n // 2, arr)
        check_quad(x + n // 2, y, n // 2, arr)
        check_quad(x, y + n // 2, n // 2, arr)
        check_quad(x + n // 2, y + n // 2, n // 2, arr)
    # 영역 내 숫자가 다 같으면 해당하는 수를 카운트해준다
    else:
        answer[arr[x][y]] += 1


def solution(arr):
    global answer
    answer = [0] * 2
    check_quad(0, 0, len(arr), arr)
    return answer

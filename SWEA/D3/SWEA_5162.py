# SW Expert Academy - 5162번. 두가지 빵의 딜레마

T = int(input())

for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    result = 0
    min_vals = [0, 0]
    if A > B:
        min_vals[0], min_vals[1] = B, A
    else:
        min_vals[0], min_vals[1] = A, B
    for num in min_vals:
        result += C // num
        C = C % num
    print('#{} {}'.format(tc, result))

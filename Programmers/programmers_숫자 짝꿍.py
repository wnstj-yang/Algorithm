def solution(X, Y):
    answer = ''
    # 각 X, Y의 딕셔너리에 숫자별 문자열 상태를 0으로 초기화
    result_X = {str(i): 0 for i in range(10)}
    result_Y = {str(i): 0 for i in range(10)}
    # 각 X와 Y의 반복문을 돌면서 해당 문자열 숫자의 개수를 더해준다
    for i in X:
        result_X[i] += 1
    for j in Y:
        result_Y[j] += 1
    # 최댓값을 만들기 위해 가장 큰 값부터 반복문을 진행
    for i in range(9, -1, -1):
        val_X, val_Y = result_X[str(i)], result_Y[str(i)]
        min_cnt = min(val_X, val_Y)
        # 예외적으로 0이 여러개가 나오면 그냥 0을 반환해준다
        if answer == '' and i == 0 and min_cnt != 0:
            return '0'
        answer = ''.join([answer, str(i) * min_cnt])
        # 기존에는 answer += str(i) * min(val_X, val_Y) 를 했는데
        # 문자열을 더해서 붙이는 경우가 시간복잡도에서 큰 비율을 차지하는 것 같아 위의 방식대로 변경함
        # 새로운 객체가 계속해서 생성되는 것이기 때문이다.

    if answer == '':
        answer = '-1'

    return answer

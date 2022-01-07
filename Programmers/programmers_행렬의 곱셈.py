def solution(arr1, arr2):
    answer = []
    # 행렬 곱셈 => 2x3 3x2 => 2x2 행렬 결과
    # 왼쪽 행렬의 행과 오른쪽 행렬의 열을 곱해준다
    for k in range(len(arr1)):
        temp = [0] * len(arr2[0]) # 만들어지는 하나의 행을 만든다
        for i in range(len(arr1[0])):
            for j in range(len(arr2[0])):
                temp[j] += arr1[k][i] * arr2[i][j]
        answer.append(temp)
    return answer

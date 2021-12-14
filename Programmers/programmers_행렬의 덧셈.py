def solution(arr1, arr2):
    # 행렬의 길이
    len1 = len(arr1)
    # 각 리스트별 길이
    len2 = len(arr1[0])
    # 각 구한 길이별로 메모리 할당
    answer = [[0] * len2 for _ in range(len1)]
    # 행렬의 덧셈
    for i in range(len1):
        for j in range(len2):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
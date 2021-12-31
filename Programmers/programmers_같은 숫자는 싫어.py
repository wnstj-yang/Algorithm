def solution(arr):
    val = arr[0]  # 처음 값을 넣는다
    answer = [val]
    for i in range(1, len(arr)):
        # 그 이후 val이란 값과 그 다음의 값이 다르다면
        # val을 초기화해주면서 다른 값을 answer에 넣어준다
        if arr[i] != val:
            val = arr[i]
            answer.append(arr[i])

    return answer
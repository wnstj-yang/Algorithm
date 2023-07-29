def solution(sequence, k):
    answer = []
    now_sum = 0  # 합을 0으로 초기화
    # 인덱스 범위 등을 고려했을 때  right를 -1로 설정하고 진행하는 것이 수월하다. 0이나 1로 하면 추가적인 코드 작성이 필요
    left, right = 0, -1  # 0부터 시작하므로 오른쪽 인덱스는 -1로 우선 초기화. 실질적으로 right을 움직여서 더한다
    # left는 단순 합을 기준으로 했을 때 옮기는 기준
    while True:
        # 2단계로 나눈다.
        # 1단계 : 합에 대한 연산과 left, right 인덱스 설정
        # 2단계 : 만들어진 합에 대해서 정답 후보로 판단

        # 목표 k보다 값이 작으면 right + 1을 해서 범위를 넓힌다.
        if now_sum < k:
            right += 1
            if right >= len(sequence):
                break
            now_sum += sequence[right]
        # k보다 크거나 같은 경우 범위를 좁혀나간다
        else:
            now_sum -= sequence[left]
            if left >= len(sequence):
                break
            left += 1

        if now_sum == k:
            answer.append((right - left, left, right))

    # 정답 후보들에 대해 정렬을 진행해서 첫번째 값을 길이가 짧고 인덱스를 넣는다
    answer.sort()
    answer = [answer[0][1], answer[0][2]]
    return answer

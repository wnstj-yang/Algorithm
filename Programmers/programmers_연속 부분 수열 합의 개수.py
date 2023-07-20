def solution(elements):
    result = set() # 집합 자료형을 써서 중복 제거
    length = len(elements) # 길이
    for i in range(1, length + 1): # 연속 부분 수열을 구할 길이로 순회
        for j in range(length):
            # 연속 부분수열을 구하면서 현재 위치에서 연속 길이만큼 더했을 때 해당 원형 수열의 길이를 벗어나지 않는 범위일 때
            if i + j < len(elements):
                result.add(sum(elements[j:i+j]))
            # 범위를 벗어난 경우 원형 길이이므로 현재 위치 + 길이 에서 원형 수열의 길이를 빼준 값까지의 합과
            # 현재 위치에서부터 원형 수열의 길이 끝까지의 합을 더해준다
            else:
                result.add(sum(elements[j:]) + sum(elements[:i+j-length]))

    return len(result)

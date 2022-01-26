def solution(land):
    answer = 0
    for i in range(len(land)-1):
        # 현재 열을 제외한 이전 행들의 열 중 최대 값을 더해 저장합니다
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    # 모두 더해진 마지막 행에서의 최대값으로 정답을 구합니다
    answer = max(land[-1])
    return answer
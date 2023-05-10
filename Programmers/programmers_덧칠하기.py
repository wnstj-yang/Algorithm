def solution(n, m, section):
    answer = 1 # 최소 1개 값은 주어진다.
    painted = section[0] # 그래서 색칠되지 않은 첫번째 부분을 m만큼 색칠했다고 가정
    for i in range(1, len(section)): # 그 이후 section부터 시작
        if section[i] - painted >= m: # 현재 section의 값과 색칠된 곳의 범위가 m보다 크거나 같다면 색칠해야한다.
            answer += 1 # 색칠 수 증가
            painted = section[i] # 증가 이후 최근 색칠된 곳의 기준을 갱신시켜 색칠된 곳의 범위를 설정한다.
    return answer

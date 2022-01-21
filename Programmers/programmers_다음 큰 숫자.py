def solution(n):
    answer = 0
    n_bin = bin(n)[2:] # n의 이진수 값
    n_cnt = n_bin.count('1') # 1의 개수를 카운트
    # 그 다음 큰 숫자부터 100만 이하 자연수 까지 target을 찾는다
    for target in range(n+1, 1000001):
        target_bin = bin(target)[2:] # 그 다음 큰 수의 이진수
        if n_cnt == target_bin.count('1'): # 1의 개수가 같다면 정답
            answer = target
            break
    return answer
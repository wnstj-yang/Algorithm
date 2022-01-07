def solution(n):
    answer = 0
    for i in range(1, n + 1):
        cnt = 0 # 연속된 수의 합
        for j in range(i, n + 1):
            cnt += j
            # n과 cnt(연속된 수의 합)가 같으면 가지 + 1 후 break
            if cnt == n:
                answer += 1
                break
            # cnt가 n보다 커지면 굳이 돌 필요가 없어서 끝
            if cnt > n:
                break
    return answer
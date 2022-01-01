def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        cnt = 0
        for i in range(1, num+1):
            # 약수라면 개수 카운트
            if num % i == 0:
                cnt += 1
        # 홀수일 때 숫자를 빼고 짝수면 더한다
        if cnt % 2:
            answer -= num
        else:
            answer += num
    return answer
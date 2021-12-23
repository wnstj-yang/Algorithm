def solution(n):
    answer = -1
    # 큰 수의 시간을 줄이기 위해 루트를 씌워서 그 수까지 진행
    for i in range(1, int(n ** 0.5)+1):
        # 1 ~ n^0.5까지의 수의 제곱이 같다면 answer + 1 후 제곱
        if i ** 2 == n:
            answer = (i + 1) ** 2
            break
    return answer
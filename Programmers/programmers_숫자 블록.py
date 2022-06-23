def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
        else:
            check = True
            # 표와 그려보았을 때 소수인 경우에는 1번 블록이 깔림
            for j in range(2, int(i ** 0.5) + 1):
                # 소수가 아닌 경우에는 j가 최소인 값과 현재 i은 값이 나누어진 블록 수가 깔린다.
                # 추가적으로 10,000,000 블록까지이므로 범위 설정
                if i % j == 0 and i // j <= 10000000:
                    answer.append(i // j)
                    check = False
                    break
            if check:
                answer.append(1)

    return answer

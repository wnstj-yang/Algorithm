def solution(prices):
    answer = []
    # 가격 길이
    length = len(prices)
    for i in range(length):
        for j in range(i + 1, length):
            # 현재 가격이 그 다음의 가격보다 크다면 다음 가격이 떨어졌으므로
            # 기간을 구한다. 끝까지 없다면 끝까지 가서 그 기간을 구한다
            if prices[i] > prices[j] or j == length - 1:
                answer.append(j - i)
                break
    # 마지막은 0으로 끝
    answer.append(0)

    return answer
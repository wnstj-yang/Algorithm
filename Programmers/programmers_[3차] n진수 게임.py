def trans_number(n, number):
    num_over_ten = {
        10: 'A', 11: 'B', 12: 'C',
        13: 'D', 14: 'E', 15: 'F',
    }
    temp = ''  # 숫자를 n진법으로 만든 수
    if number == 0:
        temp = '0'
    while number != 0:
        remainder = number % n
        if remainder in num_over_ten:
            temp = str(num_over_ten[remainder]) + temp
        else:
            temp = str(remainder) + temp
        number = number // n

    return temp


def solution(n, t, m, p):
    answer = ''
    num = 0
    # m명 만큼 한 바퀴를 돌면서 t개가 있어야 하니 길이가 m * t보다 작아야함. 크거나 같으면 t초과
    result = ''
    while len(result) < m * t:
        # 숫자를 0부터 시작해서 각 해당 숫자의 n진법 수를 구한다.
        result += trans_number(n, num)
        num += 1

    for idx in range(len(result)):
        # 길이가 완성되면 끝
        if len(answer) == t:
            break
        # 사람 명수를 나머지 연산을 통해 튜브가 구할 숫자를 택
        if idx % m == p - 1:
            answer += result[idx]

    return answer

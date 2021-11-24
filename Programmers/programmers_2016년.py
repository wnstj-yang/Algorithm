def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = 0
    # 이전 달 까지 더함
    for i in range(a-1):
        answer += months[i]
    # 1/1 금부터 시작인데 거기에 한번 더 더해서 1을 빼준다
    answer += b - 1
    answer = answer % 7
    return days[answer]
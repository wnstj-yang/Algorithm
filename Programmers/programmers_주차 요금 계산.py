import math


def solution(fees, records):
    answer = []
    car_list = {}  # 차량 번호별 정보 담을 딕셔너리
    for record in records:
        time, number, inout = record.split(' ')
        time = int(time[:2]) * 60 + int(time[3:])  # 시간을 모두 분단위로
        # 차량 번호가 주차공간에 방문하지 않았을 때 초기화, 이외는 시간을 더해준다
        if number not in car_list:
            car_list[number] = [time]
        else:
            car_list[number].append(time)

    # 순서별로 하기 위해 정렬을 해준다
    car_list = sorted(car_list.items())
    # 위의 결과로 리스트 튜플로 반환된다. [('0000', [360, 394, 1139])] 처럼
    for car in car_list:

        info = car[1]  # 입출입 시간만 있는 것
        all_time = 0

        # 홀수라면 출차되지 않았으므로 23:59에 출차됨을 가정하므로 이를 추가한다.
        if len(info) % 2 == 1:
            info.append(23 * 60 + 59)

        # 각각 입출입 시간이 리스트에 순서대로 저장되어있으므로 시간 계산
        for i in range(0, len(info), 2):
            all_time += info[i + 1] - info[i]

        # 요금표를 변수로 설정
        base_time, base_cost, unit_time, unit_cost = fees[0], fees[1], fees[2], fees[3]

        # 기본 시간보다 높으면 단위 시간으로 남은 시간을 나누어서 요금 계산
        if all_time > base_time:
            all_time -= base_time
            plus_cost = math.ceil(all_time / unit_time) * unit_cost
            answer.append(base_cost + plus_cost)
        else:
            answer.append(base_cost)

    return answer

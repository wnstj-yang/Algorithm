def solution(people, limit):
    answer = 0
    start, end = 0, len(people) - 1
    # 정렬 후 무게가 무거운 사람과 낮은 사람을 더해 제한을 살펴서
    # 구명보트 최소의 개수를 구한다.
    people.sort()
    while start <= end:
        # 맨 뒷사람(무거운 사람)과 맨 앞사람(낮은 사람) 몸무게를 더해 제한 아래이면 구명보트에 태운다
        # 태우면 앞으로 이동
        if people[end] + people[start] <= limit:
            start += 1
        end -= 1 # 뒷사람은 계속해서 구명보트 태우는 기준으로 삼는다
        answer += 1
    return answer
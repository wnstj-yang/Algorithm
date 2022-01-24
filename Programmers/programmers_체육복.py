def solution(n, lost, reserve):
    answer = n
    students = []
    # 여벌을 가진 학생이 도난당했을 때를 제외해준다
    for i in lost:
        if i in reserve:
            students.append(i)
    for i in students:
        lost.remove(i)
        reserve.remove(i)
    # 정렬을 해주어야 그리디에 맞게 최대 인원 수용 가능
    # n = 5, lost = [4, 2], reserve = [3, 5]인 경우
    lost.sort()
    reserve.sort()
    answer -= len(lost) # 도난 당한 수를 n에서 뺀다
    for i in lost:
        # 도난당한 학생이 남은 체육복을 받을 수 있다면 사람 수 추가
        if i - 1 in reserve:
            reserve.remove(i - 1)
            answer += 1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            answer += 1

    return answer
import heapq


def solution(book_time):
    answer = 1
    for i in range(len(book_time)):
        s_hour, s_minute = book_time[i][0].split(':')
        e_hour, e_minute = book_time[i][1].split(':')
        book_time[i][0] = int(s_hour) * 60 + int(s_minute)
        book_time[i][1] = int(e_hour) * 60 + int(e_minute) + 10  # 쉬는시간 추가
    book_time.sort()
    q = []
    # 힙 사용
    for start, end in book_time:
        # 비어있으면 추가
        if len(q) == 0:
            heapq.heappush(q, end)
            continue

        # 시작 시간이 이전 수업의 가장 빠르게 끝나는 시간보다 크거나 같다면 강의실 추가 X
        if start >= q[0]:
            heapq.heappop(q)
        # 그 이외의 경우 추가
        else:
            answer += 1
        heapq.heappush(q, end)  # 강의들의 끝나는 시간들
    return answer

def solution(n, times):
    answer = 0
    start = min(times)  # 최소 시간
    end = max(times) * n  # 최대 시간
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for time in times:
            cnt += (mid // time)
        # 모든 사람이 심사를 다 받거나 n보다 더많은 사람들이 받았다면 시간을 줄인다.
        if cnt >= n:
            answer = mid
            end = mid - 1
        # n만큼의 사람이 심사를 받지 못했다면 시간을 늘린다.
        else:
            start = mid + 1

    return start

def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    while left <= right:
        mid = (left + right) // 2 # 건널 수 있는 사람의 수
        under_zero_cnt = 0
        check = True
        # 도무지 이유를 모르겠으나 while문 위에 stones의 길이를 구하고 인덱스로 접근했을 때
        # 일부 테스트케이스에서 시간초과남
        for stone in stones:
            if stone - mid <= 0:
                under_zero_cnt += 1
            else:
                under_zero_cnt = 0
            # 건널 수 없는 디딤돌이 k가 됐다면 탐색 범위를 줄인다.
            if under_zero_cnt == k:
                check = False
                break
        # k 미만으로 값이 구성되면 탐색 범위를 늘린다(더 많은 사람이 건널 수 있음)
        if check:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer


######## 시간 테스트 #########

# import time
# arr = [i for i in range(100000000)]
# length = len(arr)
# mid = 10
# under_zero_cnt = 0
# start_time = time.time()
# print('range 있는 것 시간')
# for i in range(length):
#     if arr[i] - mid <= 0:
#         under_zero_cnt += 1
#     else:
#         under_zero_cnt = 0
# print(time.time() - start_time)
# print('range 없는 것 시간')
# start_time = time.time()
# for stone in arr:
#     if stone - mid <= 0:
#         under_zero_cnt += 1
#     else:
#         under_zero_cnt = 0
# print(time.time() - start_time)

# range 있는 것 시간
# 16.197898387908936
# range 없는 것 시간
# 13.314356565475464
# 경우에 따라 다르나 엄청난 차이는 없지만 차이는 존재...

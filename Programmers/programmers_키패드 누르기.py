def solution(numbers, hand):
    answer = ''
    # 키패드를 반대로해서 알아보기 쉽게 좌표 저장
    phone_nums = {
        '*': [0, 0], '0': [0, 1], '#': [0, 2],
        '7': [1, 0], '8': [1, 1], '9': [1, 2],
        '4': [2, 0], '5': [2, 1], '6': [2, 2],
        '1': [3, 0], '2': [3, 1], '3': [3, 2]
    }
    left = [0, 0] # 왼손 엄지 위치
    right = [0, 2] # 오른손 엄지 위치
    for i in numbers:
        num = str(i)
        # 눌러야할 숫자가 왼쪽에 포함된 경우
        if num in ('*', '7', '4', '1'):
            left = phone_nums[num]
            answer += 'L'
        # 눌러야할 숫자가 오른쪽에 포함된 경우
        elif num in ('#', '9', '6', '3'):
            right = phone_nums[num]
            answer += 'R'
        else:
            num_x, num_y = phone_nums[num]
            left_dist = abs(left[0] - num_x) + abs(left[1] - num_y)
            right_dist = abs(right[0] - num_x) + abs(right[1] - num_y)
            # 중앙에 있는 키패드의 경우 왼손 엄지와 오른손 엄지와의 거리를 구해서 길고 짧음을 판단
            if left_dist < right_dist:
                left = [num_x, num_y]
                answer += 'L'
            elif left_dist > right_dist:
                right = [num_x, num_y]
                answer += 'R'
            # 같다면 오른손잡이인지 왼손잡이인지 판단에 따라 누른다
            else:
                if hand == 'left':
                    left = [num_x, num_y]
                    answer += 'L'
                else:
                    answer += 'R'
                    right = [num_x, num_y]
    return answer

# Baekjoon Online Judge - 1253번. 좋다

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort() # 정렬을 통한 숫자 중복 방지
good_nums = 0
# "수의 위치가 다르면 값이 같아도 다른 수이다" =>  Ex) 0 0 0 3 3 3
# 같은 수가 여러 개 있을 때 다르다고 본다
for i in range(len(numbers)):
    cur_val = numbers[i] # 현재 숫자(일종의 타겟넘버)
    # 현재 숫자를 제외한 나머지 수들의 집합(자기 자신을 제외)
    temp_numbers = numbers[:i] + numbers[i+1:]
    start, end = 0, len(temp_numbers) - 1
    # 투 포인터를 통한 시간 절감
    while start < end:
        _sum = temp_numbers[start] + temp_numbers[end]
        if _sum == cur_val:
            good_nums += 1
            break
        # 현재 수 보다 작다면 시작점 증가
        elif _sum < cur_val:
            start += 1
        # 현재 수 보다 크다면 끝점 감소
        else:
            end -= 1
print(good_nums)

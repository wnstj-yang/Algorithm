# 프로그래머스 - 폰켓몬

def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums = set(nums)
    if len(nums) > length:
        answer = length
    else:
        answer = len(nums)
    return answer

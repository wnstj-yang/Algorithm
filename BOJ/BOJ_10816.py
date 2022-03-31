# Baekjoon Online Judge - 10816번. 숫자 카드 2

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
nums_cnt = {}
answer = []
# 딕셔너리 형태로해서 숫자 카운트를 해준다
for number in numbers:
    if number not in nums_cnt:
        nums_cnt[number] = 1
    else:
        nums_cnt[number] += 1

# 숫자가 없다면 0 아니면 그 숫자의 개수를 넣어준다
for target in targets:
    if target not in nums_cnt:
        answer.append(0)
    else:
        answer.append(nums_cnt[target])
print(*answer)

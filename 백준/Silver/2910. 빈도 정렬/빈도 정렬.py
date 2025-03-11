N, C = map(int, input().split())
num_orders = {}
num_count = {}
nums = list(map(int, input().split()))

for i in range(len(nums)):
    num = nums[i]
    if num not in num_count:
        num_count[num] = [1, i]
    else:
        num_count[num][0] += 1
result = []

orders = sorted(num_count.items(), key=lambda x:(-x[1][0], x[1][1]))
for order in orders:
    num, cnt = order[0], order[1][0]
    for _ in range(cnt):
        result.append(num)
print(*result)

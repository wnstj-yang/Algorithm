N = int(input())
orders = list(map(int, input().split()))
stack = []
order = 1
for num in orders:
    stack.append(num)
    while stack and stack[-1] == order:
        order += 1
        stack.pop()
if stack:
    print('Sad')
else:
    print('Nice')

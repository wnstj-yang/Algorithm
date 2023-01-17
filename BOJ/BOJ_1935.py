# Baekjoon Online Judge - 1935번. 후위 표기식2


N = int(input())
expression = input()
stack = []
numbers = []
for i in range(N):
    numbers.append(int(input()))

for e in expression:
    if 65 <= ord(e) <= 90:
        idx = ord(e) - ord('A')
        stack.append(numbers[idx])
    else:
        A = stack.pop()
        B = stack.pop()
        if e == '+':
            stack.append(A + B)
        elif e == '-':
            stack.append(B - A)
        elif e == '/':
            stack.append(B/A)
        else:
            stack.append(A * B)
answer = float(stack.pop())
print('{:.2f}'.format(answer))

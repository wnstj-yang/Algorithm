# Baekjoon Online Judge - 16120번. PPAP

word = input()
stack = []
for alpha in word:
    stack.append(alpha)
    if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append('P')
result = ''.join(stack)
if result == 'P' or result == 'PPAP':
    print('PPAP')
else:
    print('NP')
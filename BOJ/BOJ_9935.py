# Baekjoon Online Judge - 9935번. 문자열 폭발

string = input()
stack = []
explosion = input()
explosion_length = len(explosion)
for alpha in string:
    stack.append(alpha)
    # 폭발 문자열 길이보다 크거나 같다면 끝에서부터
    if len(stack) >= explosion_length:
        # 뒤에서 부터 폭발 문자열 길이만큼 시작해서 끝까지
        target = stack[-explosion_length:]
        # 구한 것의 문자열로 전환 시 같다면 해당 길이만큼 stack에서 빼준다
        if ''.join(target) == explosion:
            for _ in range(explosion_length):
                stack.pop()
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))


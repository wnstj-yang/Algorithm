def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        # 1. k가 0보다 크고, stack안이 값이 있다면 현재 숫자보다 작을 때 stack에서 빼준다
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    # 충분히 제거되지 않았다면 해준다. (Ex. "1000", 1 => "100" / but, 1000 return)
    while k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack)
class Solution(object):
    def removeStars(self, s):
        stack = []
        # * 표시이면 마지막 문자를 지워준다
        for string in s:
            if stack and string == '*':
                stack.pop()
            else:
                stack.append(string)
        return ''.join(stack)
        
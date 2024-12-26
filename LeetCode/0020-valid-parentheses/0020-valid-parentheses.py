class Solution(object):
    def isValid(self, s):
        stack = []
        for string in s:
            if string in ['(', '{', '[']:
                stack.append(string)
            elif stack and stack[-1] == '(' and string == ')':
                stack.pop()
            elif stack and stack[-1] == '{' and string == '}':
                stack.pop()
            elif stack and stack[-1] == '[' and string == ']':
                stack.pop()
            else:
                stack.append(-1)
                break
        if stack:
            return False
        return True
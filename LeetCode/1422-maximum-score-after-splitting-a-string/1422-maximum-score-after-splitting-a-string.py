class Solution(object):
    def maxScore(self, s):
        result = 0
        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            result = max(result, left.count('0') + right.count('1'))
        return result
        
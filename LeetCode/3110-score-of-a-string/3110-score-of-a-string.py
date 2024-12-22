class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        ascii_values = []
        for num in s:
            ascii_values.append(ord(num))
        for i in range(len(ascii_values) - 1):
            result += abs(ascii_values[i] - ascii_values[i + 1])
        return result
        
class Solution(object):
    def romanToInt(self, s):
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        N = len(s)
        for i in range(N):
            if i + 1 < N and symbols[s[i]] < symbols[s[i + 1]]:
                result -= symbols[s[i]]
            else:
                result += symbols[s[i]]
        return result

        
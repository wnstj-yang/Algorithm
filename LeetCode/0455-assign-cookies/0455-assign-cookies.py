class Solution(object):
    def findContentChildren(self, g, s):
        result = 0
        if len(s) == 0:
            return result
        g.sort(reverse=True)
        s.sort(reverse=True)
        j = 0
        for i in range(len(g)):
            if j >= len(s):
                break
            if s[j] >= g[i]:
                result += 1
                j += 1
        return result
        
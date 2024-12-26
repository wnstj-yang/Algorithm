class Solution(object):
    def longestCommonPrefix(self, strs):
        strs = sorted(strs, key=len)
        result = ''
        not_same = False
        for i in range(len(strs[0])):
            result += strs[0][i]
            for string in strs:
                if string[:i+1] != result:
                    return strs[0][:i]
        return result
        
class Solution(object):
    def groupAnagrams(self, strs):
        result = {}
        for string in strs:
            sort_string = ''.join(sorted(string))
            if sort_string not in result:
                result[sort_string] = [string]
            else:
                result[sort_string].append(string)
        return result.values()
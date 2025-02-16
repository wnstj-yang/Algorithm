class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result += 1
        return result
        
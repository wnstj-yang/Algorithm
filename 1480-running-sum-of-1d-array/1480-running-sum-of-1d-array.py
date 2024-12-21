class Solution(object):
    def runningSum(self, nums):
        sum = 0
        result = []
        for num in nums:
            sum += num
            result.append(sum)
        return result
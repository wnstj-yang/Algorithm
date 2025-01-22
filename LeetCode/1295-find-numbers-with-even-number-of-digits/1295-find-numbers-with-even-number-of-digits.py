class Solution(object):
    def findNumbers(self, nums):
        ans = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ans += 1
        return ans
        
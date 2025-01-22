class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ans = 0
        cnt = 0
        for n in nums:
            if n == 1:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans
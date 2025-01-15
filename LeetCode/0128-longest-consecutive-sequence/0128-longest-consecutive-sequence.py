class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort()
        result = 0
        cnt = 1
        for i in range(len(nums) - 1):
            num = nums[i + 1] - nums[i]
            if num == 0:
                continue
            if num == 1:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 1

        result = max(result, cnt)
        return result
        
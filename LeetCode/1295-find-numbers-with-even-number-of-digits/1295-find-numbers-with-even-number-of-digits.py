class Solution(object):
    def findNumbers(self, nums):
        ans = 0
        for num in nums:
            cnt = 0
            while num != 0:
                num = num // 10
                cnt += 1
            if cnt % 2 == 0:
                ans += 1
        return ans
        # for num in nums:
        #     if len(str(num)) % 2 == 0:
        #         ans += 1
        # return ans
        
class Solution(object):
    def isArraySpecial(self, nums):
        # different parity -> 서로 다른 홀짝 여부. 즉, 둘 다 홀수이거나 짝수이면 안된다.
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
        
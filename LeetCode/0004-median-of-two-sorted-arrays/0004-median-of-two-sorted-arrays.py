class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        # 개수가 홀수인 경우
        if length % 2:
            return nums[length // 2]
        # 개수가 짝수인 경우
        else:
            mid = length // 2
            # _sum = nums[mid - 1] + nums[mid]
            return float(nums[mid - 1] + nums[mid]) / 2
        
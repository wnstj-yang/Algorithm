class Solution(object):
    def topKFrequent(self, nums, k):
        nums_list = {}
        for num in nums:
            if num not in nums_list:
                nums_list[num] = 1
            else:
                nums_list[num] += 1
        sorted_nums = sorted(nums_list.items(), key=lambda x: -x[1])
        result = [num[0] for num in sorted_nums[:k]]
        return result
        
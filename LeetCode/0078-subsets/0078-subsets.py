class Solution(object):
    def subsets(self, nums):
        result = [[]]
        def get_subset(index, cnt, k, num, visited):
            if cnt == k:
                result.append(list(num))
                return
            for i in range(index, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    num[cnt] = nums[i]
                    get_subset(i + 1, cnt + 1, k, num, visited)
                    visited[i] = False
        for i in range(1, len(nums) + 1):
            num = [0] * i
            visited = [False] * len(nums)
            get_subset(0, 0, i, num, visited)
        return result
        
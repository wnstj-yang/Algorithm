class Solution(object):
    def perm(self, idx, result, visited, arr, ans):
        if len(result) == len(arr):
            ans.append(result[:])
            return
        
        # 순열의 경우 모든 요소에서 백트래킹을 활용해야 한다.
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                result.append(arr[i])
                self.perm(i + 1, result, visited, arr, ans)
                result.pop()
                visited[i] = False

    def permute(self, nums):
        ans = []
        visited = [False] * len(nums)
        self.perm(0, [], visited, nums, ans)
        return ans
        
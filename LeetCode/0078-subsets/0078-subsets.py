class Solution(object):
    def subsets(self, nums):
        result = []
        # 수식을 따라 직접 손으로 해보면 이런 형태구나 라는 인식이 가능
        # 1 << n => 2^n, 즉 배열의 길이
        for bit in range(1 << len(nums)):
            subset = []
            # 비트마스크 연산
            for i in range(len(nums)):
                # 1인 부분이 and연산으로 해서 부분집합을 구한다
                if bit & (1 << i):
                    subset.append(nums[i])
            result.append(subset)
        return result
        
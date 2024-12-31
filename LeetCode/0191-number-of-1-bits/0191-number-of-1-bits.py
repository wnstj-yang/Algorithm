class Solution(object):
    def hammingWeight(self, n):
        cnt = 0
        for num in bin(n)[2:]:
            if num == '1':
                cnt += 1
        return cnt
        
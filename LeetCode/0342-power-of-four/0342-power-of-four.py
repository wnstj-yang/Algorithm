class Solution(object):
    def isPowerOfFour(self, n):
        if n > 0 and n & (n - 1) == 0:
            return True
        return False
        
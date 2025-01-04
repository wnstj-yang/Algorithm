class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0: return False
        while True:
            if n == 1:
                break
            if n % 2 == 1:
                return False
            n = n // 2
        return True
        
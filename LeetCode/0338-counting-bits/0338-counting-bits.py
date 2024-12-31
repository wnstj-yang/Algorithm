class Solution(object):
    def countBits(self, n):
        result = []
        for num in range(n + 1):
            int_to_bin = bin(num)[2:]
            result.append(int_to_bin.count('1'))
        return result
        
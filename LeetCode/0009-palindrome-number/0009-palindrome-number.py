class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = str(x)
        N = len(num) - 1
        for i in range(len(num) // 2):
            if num[i] != num[N]:
                return False
            N -= 1
        return True
        
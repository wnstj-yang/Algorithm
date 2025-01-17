class Solution(object):
    def addDigits(self, num):
        num = str(num)
        while len(num) > 1:
            num_sum = 0
            for n in str(num):
                num_sum += int(n)
            num = str(num_sum)
        return int(num)
        
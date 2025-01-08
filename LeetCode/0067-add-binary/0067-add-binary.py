class Solution(object):

    def calculate(self, string):
        num = 1
        cnt = 0
        for b in string:
            if b == '1':
                cnt += num
            num *= 2
        return cnt

    def addBinary(self, a, b):
        first = self.calculate(a[::-1])
        second = self.calculate(b[::-1])
        result = first + second
        return bin(result)[2:]

        
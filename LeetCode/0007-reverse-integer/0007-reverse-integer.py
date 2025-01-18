class Solution(object):

    def check_range(self, num):
        if -2 ** 31 <= num <= 2 ** 31 - 1:
            return True
        else:
            return False

    def reverse(self, x):
        reverse_num = ''.join(reversed(str(x)))
        result = 0
        if reverse_num[-1] == '-':
            result = -int(reverse_num[:-1])
        else:
            result = int(reverse_num)
        if self.check_range(result):
            return result
        else:
            return 0
        
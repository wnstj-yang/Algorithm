class Solution(object):
    def reverse(self, x):
        is_sign = 1 if x > 0 else -1
        x = abs(x)
        ans = 0
        # 자리수를 판단하므로 마지막 자리수부터 시작해서 앞으로 추가해주는 방식
        while x != 0:
            ans = ans * 10 + x % 10
            x //= 10

        if -2 ** 31 <= is_sign * ans <= 2 ** 31 - 1:
            return is_sign * ans
        else:
            return 0
        

    # 직접 reverse를 해주고 진행
    # def check_range(self, num):
    #     if -2 ** 31 <= num <= 2 ** 31 - 1:
    #         return True
    #     else:
    #         return False

    # def reverse(self, x):
    #     reverse_num = ''.join(reversed(str(x)))
    #     result = 0
    #     if reverse_num[-1] == '-':
    #         result = -int(reverse_num[:-1])
    #     else:
    #         result = int(reverse_num)
    #     if self.check_range(result):
    #         return result
    #     else:
    #         return 0
        
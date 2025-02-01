class Solution(object):
    def isHappy(self, n):
        if n == 1 or n == 7:
            return True
        elif n < 10:
            return False
        else:
            num = 0
            while n > 0:
                number = n % 10
                num += (number * number)
                n //= 10
            return self.isHappy(num)

        
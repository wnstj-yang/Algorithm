class Solution(object):
    def isHappy(self, n):
        # 규칙이 존재 -> n이 1이나 7이면 True이다.
        # 그외 한 자리수의 경우에는 False
        # 지속적으로 한자리 수에서 곱하고 나누면서 과정을 거쳐야하기 때문에 재귀를 활용
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

        
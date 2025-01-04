class Solution(object):
    def isPowerOfTwo(self, n):
        # n은 2의 제곱수에 속한다면 비트로 단 하나의 1만 가진다.
        # n - 1은 n을 제외하고 오른쪽의 비트가 모두 1이다.
        # 이 둘을 AND연산 했을 때 모두 0이 나온다면 2의 제곱수에 맞는 것이다.
        result = n & (n - 1)
        if n > 0 and result == 0:
            return True
        return False
        
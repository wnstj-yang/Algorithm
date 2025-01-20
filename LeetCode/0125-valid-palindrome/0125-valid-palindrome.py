class Solution(object):
    def isPalindrome(self, s):
        result = ''
        for string in s.lower():
            # 알파벳 혹은 숫자를 포함하므로 isalpha -> isalnum 메서드활용
            if string.isalnum():
                result += string
        l, r = 0, len(result) - 1
        while l < r:
            if result[l] != result[r]:
                return False
            l += 1
            r -= 1
        return True
        
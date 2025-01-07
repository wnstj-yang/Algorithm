class Solution(object):
    def isAnagram(self, s, t):
        alpha_count = [0] * 26 # 알파벳 
        for c in s:
            alpha_count[ord(c) - ord('a')] += 1
        # 비교를 할 t문자열에서 문자들의 수가 0이면 
        for c in t:
            # 
            if alpha_count[ord(c) - ord('a')] == 0:
                return False
            alpha_count[ord(c) - ord('a')] -= 1
        if sum(alpha_count) > 0:
            return False
        return True
        
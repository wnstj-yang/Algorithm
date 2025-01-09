class Solution(object):
    def prefixCount(self, words, pref):
        cnt = 0
        pref_length = len(pref)
        for word in words:
            if len(word) >= pref_length and word[:pref_length] == pref:
                cnt += 1
        return cnt
        
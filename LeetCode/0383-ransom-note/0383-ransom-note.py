class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom = {}
        maga = {}
        for m in magazine:
            if m not in maga:
                maga[m] = 1
            else:
                maga[m] += 1
        for r in ransomNote:
            if r not in maga or maga[r] == 0:
                return False
            maga[r] -= 1
                
        return True
        
        
        
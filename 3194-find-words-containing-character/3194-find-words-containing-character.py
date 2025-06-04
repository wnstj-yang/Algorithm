class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        result = []
        for i in range(len(words)):
            word = words[i]
            if x in word:
                result.append(i)
        return result

            
        
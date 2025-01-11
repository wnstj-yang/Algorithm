class Solution(object):
    def wordSubsets(self, words1, words2):
        result = []
        word2_max = [0] * 26
        # 최대를 구하는 것은 words2의 각 word에서 알파벳 개수가 최대인 것을 기준으로 subset를 파악하기 위함이다
        for word in words2:
            word_list = [0] * 26
            for w in word:
                word_list[ord(w) - ord('a')] += 1
            for i in range(26):
                word2_max[i] = max(word2_max[i], word_list[i])
        for word in words1:
            word_list = [0] * 26
            is_right = True
            for w in word:
                word_list[ord(w) - ord('a')] += 1
            for i in range(26):
                if word_list[i] < word2_max[i]:
                    is_right = False
                    break
            if is_right:
                result.append(word)
        return result
        
        
        
            
        
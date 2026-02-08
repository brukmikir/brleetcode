class Solution(object):
    def commonChars(self, words):
        from collections import Counter
        
        common = Counter(words[0])
        
        for word in words[1:]:
            common &= Counter(word)
        
        result = []
        for char, freq in common.items():
            result.extend([char] * freq)
        
        return result

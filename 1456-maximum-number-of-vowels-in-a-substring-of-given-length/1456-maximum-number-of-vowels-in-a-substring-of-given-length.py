class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        cur = 0
        ans = 0

        for i in range(len(s)):
            if s[i] in vowels:
                cur += 1

            if i >= k and s[i-k] in vowels:
                cur -= 1

            if i >= k-1:
                ans = max(ans, cur)

        return ans
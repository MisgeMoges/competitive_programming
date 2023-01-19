class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mx = 0
        vowel = "aeiou"
        start = 0
        count = 0
        for end in range(len(s)):
            if s[end] in vowel:
                count += 1
            if end - start + 1 == k:
                mx = max(mx, count)
                if s[start] in vowel:
                    count -= 1
                start += 1
                
           
           
        return mx
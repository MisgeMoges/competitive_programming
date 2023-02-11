class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {"a", "e", "i", "o", "u", "A", "U", "E", "O", "I"}
        
        s = list(s)
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] in vowel and s[right] in vowel:
                s[left], s[right] = s[right], s[left]
                right -= 1
                left += 1
            elif s[left] not in vowel:
                left += 1
            else:
                right -= 1
        
        return "".join(s)
        
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = sum(c.isupper() for c in word)
        return count == len(word) or count == 0 or count == 1 and word[0].isupper()
        
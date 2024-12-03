class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)
        for char in ransomNote:
            if magazine_count[char] > 0:
                magazine_count[char] -= 1
            else:
                return False
        
        return True
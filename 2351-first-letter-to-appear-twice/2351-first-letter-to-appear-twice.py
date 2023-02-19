class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        hashSet = set()
        for cha in s:
            if cha in hashSet:
                return cha
            hashSet.add(cha)
        return ""
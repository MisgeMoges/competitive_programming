class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        def is_single_row(word):
            chars = set(word.lower())
            
            return chars.issubset(row1)or chars.issubset(row2)or chars.issubset(row3)
        return [word for word in words if is_single_row(word)]
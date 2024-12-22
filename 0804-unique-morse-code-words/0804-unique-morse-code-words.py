class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."]
        
        transformations = set()
        
        for word in words:
            
            transform = ''.join(morse_code[ord(char)-ord('a')] for char in word)
            transformations.add(transform)
        return len(transformations)
            
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_plate = Counter(char.lower() for char in licensePlate if char.isalpha())
        
        shortest_word = None
        
        for word in words:
            
            word_count = Counter(word)
            if all(word_count[char] >= license_plate[char] for char in license_plate):
                if shortest_word is None or len(shortest_word) > len(word):
                    shortest_word = word
        return shortest_word
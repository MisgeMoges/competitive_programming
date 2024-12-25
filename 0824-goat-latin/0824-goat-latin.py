class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        goat_latin = []

        for i, word in enumerate(words, 1):
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            # Add 'a' repeated i times
            new_word += "a" * i
            goat_latin.append(new_word)

        return " ".join(goat_latin)

                
        
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = re.findall(r'\w+', paragraph.lower())
        
        word_count = Counter(words)
        
        banned_set = set(banned)
        max_count = 0
        most_common_word= ""
        for word, count in word_count.items():
            if word not in banned_set and count > max_count:
                most_common_word = word
                max_count = max(max_count, count)
        
        return most_common_word
        
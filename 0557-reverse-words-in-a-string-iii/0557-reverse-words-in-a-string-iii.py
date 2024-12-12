class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return " "
        word_list=s.split()
        result = []
        for i in range(len(word_list)):
            result.append(word_list[i][::-1])
        return ' '.join(result)
            
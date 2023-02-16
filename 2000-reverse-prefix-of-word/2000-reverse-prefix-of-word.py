# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         left, right = 0, 0
#         word = list(word)
#         while right < len(word):
#             if ch == word[right]:
#                 while left < right and right > 0:
#                     word[left], word[right] = word[right], word[left]
#                     right -= 1
#                     left += 1
#                 return "".join(word)
#             right += 1
#         return "".join(word)
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            idx = word.index(ch)
            w = word[:idx + 1]
            return w[::-1] + word[idx + 1:]
        except: return word
        
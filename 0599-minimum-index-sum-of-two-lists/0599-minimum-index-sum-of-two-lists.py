class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map1 = {word: i for i, word in enumerate(list1)}
        min_index_sum = float('inf')
        result = []
        
        for i, word in enumerate(list2):
            if word in index_map1:
                index_sum = i + index_map1[word]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [word]
                elif index_sum == min_index_sum:
                    result.append(word)
      
        return result
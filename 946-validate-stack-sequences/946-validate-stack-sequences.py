class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped_index = 0
        len_popped = len(popped)
        for num in pushed:
            stack.append(num)
            while stack and popped_index < len_popped and  stack[-1] == popped[popped_index]:
                
                stack.pop()
                popped_index += 1
            
        return stack == []
                
            
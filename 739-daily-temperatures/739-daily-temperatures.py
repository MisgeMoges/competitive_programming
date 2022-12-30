class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        size = len(temperatures)
        stack = []
        ans = [0]*size
        
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                ans[stackIndex] = (i-stackIndex) 
           
                
                
            stack.append([t, i])
        
        return ans     
            
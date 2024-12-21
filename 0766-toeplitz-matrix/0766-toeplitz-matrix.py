class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        previous_row = None
        
        for current_row in matrix:
            if previous_row:
                for j in range(len(current_row)-1):
                    if previous_row[j] != current_row[j+1]:
                        return False
            previous_row = current_row
        return True
                    
        
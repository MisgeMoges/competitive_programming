# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
        
#         pascal_triangle = []
#         for i in range(numRows):
#             row = [1]
#             if pascal_triangle:
#                 prev_row = pascal_triangle[-1]
#                 for j in range(1, len(prev_row)):
#                     row.append(prev_row[j - 1] + prev_row[j])
#                 row.append(1)
#             pascal_triangle.append(row)
#         return pascal_triangle
                    
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows
        
        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
        
        prevRows.append(newRow)
        return prevRows

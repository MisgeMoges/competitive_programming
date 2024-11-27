class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal_triangle = []
        for i in range(numRows):
            row = [1]
            if pascal_triangle:
                prev_row = pascal_triangle[-1]
                for j in range(1, len(prev_row)):
                    row.append(prev_row[j - 1] + prev_row[j])
                row.append(1)
            pascal_triangle.append(row)
        return pascal_triangle
                    
            
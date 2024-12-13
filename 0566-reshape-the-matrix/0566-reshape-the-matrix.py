class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # Check if the reshape operation is possible
        if m * n != r * c:
            return mat

        # Flatten the matrix
        flat_list = [num for row in mat for num in row]

        # Build the reshaped matrix
        reshaped_matrix = [flat_list[i * c:(i + 1) * c] for i in range(r)]

        return reshaped_matrix
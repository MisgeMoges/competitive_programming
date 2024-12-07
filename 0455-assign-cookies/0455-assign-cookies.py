class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # Sort greed factors
        s.sort()  # Sort cookie sizes

        i, j = 0, 0  # Pointers for children and cookies
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # Cookie satisfies the child
                i += 1  # Move to the next child
            j += 1  # Move to the next cookie

        return i  # The number of satisfied children

                
        
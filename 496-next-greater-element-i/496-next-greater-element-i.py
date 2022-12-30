class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1Index = {n:i for i, n in enumerate(nums1)}
        res = [-1]*len(nums1)
        
        stack = []
        for i in range(len(nums2)):
            current = nums2[i]
            while stack and current > stack[-1]:
                val = stack.pop()
                index = nums1Index[val]
                res[index] = current
            if current in nums1Index:
                stack.append(current) 

        return res

        



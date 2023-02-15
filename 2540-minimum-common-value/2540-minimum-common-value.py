class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
       
        intersect =list(set( nums1).intersection(set(nums2)))
        if len(intersect) == 0:
            return -1
        minValue = intersect[0]
        for i in range(1, len(intersect)):
            minValue = min(minValue, intersect[i])
        return minValue
        
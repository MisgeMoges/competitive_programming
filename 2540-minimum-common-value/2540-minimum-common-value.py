class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        intersect = nums1.intersection(nums2)
        if len(intersect) == 0:
            return -1
        intersect = list(intersect)
        minValue = intersect[0]
        for i in range(1, len(intersect)):
            minValue = min(minValue, intersect[i])
        return minValue
        
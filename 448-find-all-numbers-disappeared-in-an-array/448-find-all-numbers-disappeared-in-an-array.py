class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums = set(nums)
        nums1 = []
        for i in range(1, N+1):
            nums1.append(i)
        return list(set(nums1)-nums)
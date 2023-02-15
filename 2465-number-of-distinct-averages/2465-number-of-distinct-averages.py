class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
      
        ans = []
        for i in range(len(nums)//2):
            ans.append((max(nums)+min(nums))/2)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return len(set(ans))
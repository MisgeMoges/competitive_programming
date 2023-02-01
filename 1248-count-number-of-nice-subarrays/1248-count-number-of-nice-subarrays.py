class Solution:
	def numberOfSubarrays(self, nums: List[int], k: int) -> int:
		n = len(nums)
		nums = [num % 2 for num in nums]
		ones = [-1] + [i for i in range(n) if nums[i] == 1] + [n]
		cnt = 0
		i = 1
		j = k
		while j < len(ones) - 1:
			cnt += (ones[j+1] - ones[j]) * (ones[i] - ones[i-1])
			j += 1
			i += 1
		return cnt
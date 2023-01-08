class Solution:
	def findTheWinner(self, n: int, k: int) -> int:
		def solve(listVal, k, target):
			if len(listVal)==1:
				return listVal[-1]
			listVal.pop(target)
			length = len(listVal)
			target = (target+k-1)%length
			return solve(listVal,k,target)
		listValue = list(range(1, n+1))
		targetToCheck = (0+k-1)%n
		ans = solve(listValue, k, targetToCheck)
		return ans
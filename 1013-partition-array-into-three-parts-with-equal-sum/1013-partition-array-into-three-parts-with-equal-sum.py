class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        prefixSum = sum(arr)
        count = 0
        sum_ = 0
        if prefixSum % 3 == 0:
            for i in range(len(arr)):
                sum_ += arr[i]
                if sum_ == prefixSum / 3:
                    sum_ = 0
                    count += 1
            if count >= 3:
                return True
            else:
                return False
        else:
            return False
                
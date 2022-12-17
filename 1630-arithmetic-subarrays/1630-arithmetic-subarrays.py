class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        
        # output = []
        
        output = []

        for x, y in zip(l, r):
            temp = sorted(nums[x:y+1])
            check = temp[1] - temp[0]
            for i in range(len(temp) - 1):
                const = temp[i+1] - temp[i]
                if const != check:
                    feed = False
                    break
                else:
                    feed = True
            output.append(feed)
        
        return output

       
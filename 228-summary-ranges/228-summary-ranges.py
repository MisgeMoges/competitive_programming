class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        if n==0:
            return []
        if n==1:
            return [str(nums[0])]
        #two pointer
        i = 0
        while(i<n):
            start = end = nums[i]
            curr = str(start)
            j = i+1
            while(j<n and nums[j]-nums[i]==1):
                end = nums[j]
                j+=1   
                i+=1
            if start!=end:
                curr = str(start)+"->"+str(end)
            i+=1
            
            res.append(curr)
        return res
        
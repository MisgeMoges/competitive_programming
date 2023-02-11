class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p, len_s,ans = len(p), len(s), []
        p = Counter(p)
        window = None
        for i in range(0, len_s-len_p + 1):
            if i == 0:
                window = Counter(s[:len_p])
            else:
                window[s[i-1]] -= 1
                window[s[i+len_p-1]] += 1
            if len(window - p) == 0:
                ans.append(i)
        return ans
    
 
                
            
                
                
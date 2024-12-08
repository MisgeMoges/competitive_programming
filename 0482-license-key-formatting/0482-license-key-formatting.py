class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = s.replace("-", "").upper()
        first_group_size = len(s)%k
        
        result = []
        
        if first_group_size:
            result.append(s[:first_group_size])
            
        for i in range(first_group_size, len(s), k):
            result.append(s[i:i+k])
            
        return "-".join(result)
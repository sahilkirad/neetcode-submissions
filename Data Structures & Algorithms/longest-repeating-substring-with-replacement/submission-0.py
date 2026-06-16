class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        left=0
        ans=0
        
        # for i in s:
        #     ht[i]=ht.get(i,0)+1
        # if len(set(ht.values())) <= 1:
        #     return len(s)
        
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq=max(freq.values()) 
            while (right - left + 1) - max_freq > k:
                freq[s[left]]-=1
                left += 1
                max_freq=max(freq.values()) 
            
            ans=max(ans,right-left+1)
        return ans

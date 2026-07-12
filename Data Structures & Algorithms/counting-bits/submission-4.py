class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # i & (i - 1) gives us a smaller number that we already calculated.
            ans[i] = ans[i>>1] + (i&1)
            
        return ans

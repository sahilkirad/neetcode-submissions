class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # i & (i - 1) gives us a smaller number that we already calculated.
            # We just add 1 to that past answer because we know we dropped exactly one '1' bit.
            ans[i] = ans[i & (i - 1)] + 1
            
        return ans

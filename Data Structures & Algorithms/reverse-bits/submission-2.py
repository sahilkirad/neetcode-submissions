class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for _ in range(32):
            rem=n&1
            res=res<<1
            res=res|rem
            n=n>>1
        
        return res
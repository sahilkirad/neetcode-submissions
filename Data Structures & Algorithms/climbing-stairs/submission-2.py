class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        else:
            prev=1
            prev2=1
            for i in range(2,n+1):
                curi=prev+prev2
                prev2=prev
                prev=curi
        
        return curi
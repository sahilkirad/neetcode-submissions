class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            print(0)
        else:
            prev=1
            prev2=0
            for i in range(2,n+1):
                curi=prev+prev2
                prev2=prev
                prev=curi
        
        return prev+1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
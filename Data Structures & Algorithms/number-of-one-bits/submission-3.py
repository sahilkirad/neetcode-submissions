class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n!=0:
            # rem=n&1
            # if rem==1:
            #     count+=1
            # n=n>>1
            n=n&(n-1)
            count=count+1
        return count
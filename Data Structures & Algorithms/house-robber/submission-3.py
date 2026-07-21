class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        # edge case
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        
        # detech neighbours and do not compute it in ans max
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            rob=nums[i] + dp[i-2]
            skip=dp[i-1]
            dp[i]=max(rob,skip)
        
        return dp[len(nums)-1]

            
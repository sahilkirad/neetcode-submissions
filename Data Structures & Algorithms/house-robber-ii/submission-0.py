def helper(nums):
    dp=[0]*len(nums)
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])
    for i in range(2,len(nums)):
        rob=dp[i-2]+nums[i]
        skip=dp[i-1]
        dp[i]=max(rob,skip)
    return dp[-1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        dp_1=helper(nums[:-1]) #exlcude last
        dp_2=helper(nums[1:])  #include last
        
        
        return max(dp_1,dp_2)
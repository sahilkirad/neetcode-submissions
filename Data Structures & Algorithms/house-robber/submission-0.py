class Solution:
    def rob(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            if i%2==0:
                ans+=nums[i]
        return ans
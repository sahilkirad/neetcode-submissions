class Solution:
    def rob(self, nums: List[int]) -> int:
        ans=0
        if len(nums)>2:
            for i in range(len(nums)):
                if i%2==0:
                    ans+=nums[i]
            return ans
        else:
            if len(nums)==1:
                ans+=nums[0]
            else:
                ans+=nums[1]
            
            return ans
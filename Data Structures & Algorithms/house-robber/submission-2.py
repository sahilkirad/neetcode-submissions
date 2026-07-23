class Solution:
    def rob(self, nums: List[int]) -> int:
        ans=0
        # edge case
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        
        # detech neighbours and do not compute it in ans max
        if len(nums)%2==0:
            prev=0
            curr=1
            nxt=2
            for i in range(3,len(nums)):
                if nums[nxt]+nums[prev]>ans:
                    ans=nums[nxt]+nums[prev]
                prev=curr
                curr=nxt
                nxt=i
            return ans
        else:
            for i in range(len(nums)):
                if i%2==0:
                    ans+=nums[i]
            return ans

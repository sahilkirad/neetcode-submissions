class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        if not  nums:
            return 0
        nums=set(nums)
        for i in nums:
            if i-1 not in nums:
                length=0
                j=i
                while j in nums:
                    j=j+1
                    length+=1
                ans=max(ans,length)
        
        return ans
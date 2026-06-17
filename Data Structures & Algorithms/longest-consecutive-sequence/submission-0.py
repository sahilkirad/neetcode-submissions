class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        count=0
        while(i<j):
            ans=nums[i]+1
            if(nums[j]==ans):
                count+=1
                i=i+1
                j=j-1
        return count

        
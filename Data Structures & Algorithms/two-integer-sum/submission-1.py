class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aer=[]
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    aer.extend([i,j])
        aer.sort()
        return aer
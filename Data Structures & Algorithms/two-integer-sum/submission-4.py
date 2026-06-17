class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aer=[]
        aer.sort()
        i=0
        j=len(nums)-1
        while(i<j):
            if(nums[i]+nums[j]==target):
                aer.extend([i,j])
                break
            if(nums[i]+nums[j]<target):
                i=i+1
            else:
                j=j-1
        aer.sort()
        return aer
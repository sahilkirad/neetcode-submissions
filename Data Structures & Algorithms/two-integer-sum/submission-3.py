class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aer=[]
        i=0
        j=len(nums)-1
        while(i<j):
            if(nums[i]<0 or nums[j]<0):
                nums[i]=nums[i]*-1
                nums[j]=nums[j]*-1
            if(nums[i]+nums[j]==target):
                aer.extend([i,j])
                break
            if(nums[i]+nums[j]<target):
                i=i+1
            else:
                j=j-1
        aer.sort()
        return aer
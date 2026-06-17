class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        for i in range(len(nums)-1):
            j=i+1
            if nums[j] - nums[i] == 1:
                count+=1
        return count
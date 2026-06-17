class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        count=1
        for i in range(len(nums)-1):
            j=i+1
            if nums[j] - nums[i] == 1:
                count+=1
        return count
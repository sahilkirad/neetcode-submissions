class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,ele in enumerate(nums):
            found=target-ele
            if found in seen:
                return [seen[found],i]
            seen[ele]=i
                
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expe=(n * (n+1)) // 2
        ac=sum(nums)
        return expe-ac

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[left]==target:
                return left
            elif nums[mid]>target:
                left=mid+1
                continue
            else:
                right=mid
                continue
            
        return -1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        for i in range(0,len(nums)+1):
            if freq.get(i,0)==0:
                return i

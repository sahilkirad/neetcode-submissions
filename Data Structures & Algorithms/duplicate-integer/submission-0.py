class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res={}
        for i in nums:
            res[i]=res.get(i,0)+1
            if res[i]>1:
                return True
        return False
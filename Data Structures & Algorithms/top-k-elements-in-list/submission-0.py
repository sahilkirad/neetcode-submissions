from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        for i in nums:
            res[i]=res.get(i,0)+1
        res=list(dict(sorted(res.items(),key=itemgetter(1), reverse=True)))
        return res[:2]
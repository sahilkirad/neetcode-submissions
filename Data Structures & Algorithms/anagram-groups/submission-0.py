class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i,ele in enumerate(strs):
            a=ele
            key="".join(sorted(ele))
            if key in res:
                res[key].append(a)
                continue
            res[key]=[ele]
        
        return list(res.values())
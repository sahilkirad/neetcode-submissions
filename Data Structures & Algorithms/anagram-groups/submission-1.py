class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i,ele in enumerate(strs):
            key="".join(sorted(ele))
            if key in res:
                res[key].append(ele)
                continue
            res[key]=[ele]
        
        return list(res.values())
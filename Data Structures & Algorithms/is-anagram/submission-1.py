class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res={}
        
        if(len(s)!=len(t)):
                return False
        for cha in s:
            res[cha]=res.get(cha,0)+1
        r1={}
        for c in t:
            r1[c]=r1.get(c,0)+1
        
        return res==r1
            
        
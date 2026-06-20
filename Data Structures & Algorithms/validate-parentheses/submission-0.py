class Solution:
    def isValid(self, s: str) -> bool:
        res=[]
        for i in s:
            if i=='[' or i=='{' or i=='(':
                res.append(i)
                continue
            else:
                if not res:
                    return False
                ch=res[-1]
                res.pop()
                if(ch=='[' and i==']'):
                    continue
                if(ch=='{' and i=='}'):
                    continue
                if(ch=='(' and i==')'):
                    continue
                else:
                    return False
        return True
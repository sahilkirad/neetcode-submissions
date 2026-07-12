class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        ans=[]
        for i in range(n+1):
            numb=i
            c=0
            while numb>0:
                rem=numb & 1
                if rem==1:
                    c+=1
                numb=numb>>1
            ans.append(c)
        
        return ans


        
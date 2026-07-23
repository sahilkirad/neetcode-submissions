class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b!=0:
            sumy=a ^ b
            carry=(a & b) <<1
            a=sumy
            b=carry
        return a

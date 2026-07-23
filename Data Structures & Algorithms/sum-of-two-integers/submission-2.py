class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b!=0:
            sumy=(a ^ b) & MASK
            carry=((a & b) <<1) & MASK
            a=sumy
            b=carry
        return a

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_a=0
        while(i<j):
            width=j-i
            height=min(heights[i],heights[j])
            area=width*height
            max_a=max(area,max_a)
            if(heights[i]<heights[j]):
                i=i+1
            else:
                j=j-1
        return max_a
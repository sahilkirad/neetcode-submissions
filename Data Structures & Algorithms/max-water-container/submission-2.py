class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        area=None
        while(i<j):
            width=j-i
            height=min(heights[i],heights[j])
            max_a=area
            area=width*height
            area=max(area,max_a)
            if(heights[i]<heights[j]):
                i=i+1
            else:
                j=j-1
        return area
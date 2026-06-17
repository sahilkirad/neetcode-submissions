class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return heights[len(heights)-1]*heights[len(heights)-1]
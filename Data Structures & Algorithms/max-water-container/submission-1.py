class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea = 0

        while left < right:
            if heights[left] < heights[right]:
                maxArea = max(maxArea, heights[left]*(right-left))
                left += 1
            else:
                maxArea = max(maxArea, heights[right]*(right-left))
                right -= 1
        return maxArea
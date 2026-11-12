class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maximum = 0

        for i, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > height:
                popped_height = heights[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                maximum = max(maximum, popped_height * width)

            stack.append(i)

        return maximum
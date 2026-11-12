class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        current_maximum = 0
        unique_heights = set()
        unique_heights_stack = []
        for height in heights:
            if height not in unique_heights:
                unique_heights.add(height)
                unique_heights_stack.append(height)

        # for each unique height, see how many in a row
        while unique_heights:
            h = unique_heights.pop()
            longest_contiguous = 0
            current = 0
            for height in heights:
                if height >= h:
                    current += 1
                else:
                    longest_contiguous = max(current, longest_contiguous)
                    current = 0
            longest_contiguous = max(current, longest_contiguous)
            current_maximum = max(h * longest_contiguous, current_maximum)
        return current_maximum
        
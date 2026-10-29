from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        window = deque()

        for right in range(len(nums)):
            # Remove indices outside the current window
            while window and window[0] <= right - k:
                window.popleft()

            # Remove smaller values that cannot become a maximum
            while window and nums[window[-1]] <= nums[right]:
                window.pop()

            window.append(right)

            if right >= k - 1:
                output.append(nums[window[0]])

        return output
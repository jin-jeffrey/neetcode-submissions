class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        window = {}
        left = 0
        right = 0

        while right < len(nums):
            window[nums[right]] = window.get(nums[right], 0) + 1
            if right - left + 1 > k:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            if right - left + 1 == k:
                output.append(max(window.keys()))
            right += 1
        
        return output
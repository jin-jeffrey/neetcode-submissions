class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        longest = 1
        current = 1
        for i in range(len(nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                current += 1
                longest = max(longest, current)
            elif sorted_nums[i] == sorted_nums[i-1]:
                continue
            else:
                current = 1
        return longest
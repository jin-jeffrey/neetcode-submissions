class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in indices:
                return [indices[complement], i]
            indices[num] = i
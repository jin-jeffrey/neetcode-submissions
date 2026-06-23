class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = set()
        for target_index in range(len(nums)):
            left = target_index + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[left] + nums[right] + nums[target_index]
                if current_sum == 0:
                    results.add((nums[target_index], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

        return [list(x) for x in results]
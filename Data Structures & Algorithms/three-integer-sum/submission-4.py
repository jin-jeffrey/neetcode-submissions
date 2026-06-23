class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for target_index in range(len(nums)):

            if target_index > 0 and nums[target_index] == nums[target_index-1]:
                continue
                
            left = target_index + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[left] + nums[right] + nums[target_index]
                if current_sum == 0:
                    results.append([nums[target_index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # handle duplicates
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

        return results
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = set()
        for i in nums:
            if i in existing:
                return True
            existing.add(i)
        return False
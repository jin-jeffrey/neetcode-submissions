class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase and remove nonalphanumeric
        s = s.lower()
        filtered = ""
        for i in range(len(s)):
            if s[i].isalnum():
                filtered += s[i]
        
        left = 0
        right = len(filtered) - 1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True
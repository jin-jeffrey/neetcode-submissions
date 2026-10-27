class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # keep moving right pointer until there is a duplicate
        # move left pointer until the duplicate is removed
        # update viewed values constantly
        seen_values = [0] * 127
        left = 0
        right = 1
        seen_values[ord(s[left])] += 1
        longestSubstring = 0
        while right < len(s):
            # if right is not seen, then update seen list
            if seen_values[ord(s[right])] == 0:
                seen_values[ord(s[right])] += 1
                longestSubstring = max(right - left, longestSubstring)
            # if right is seen, then update move left right until duplicate is removed
            else:
                while s[left] != s[right]:
                    seen_values[ord(s[left])] -= 1
                    left += 1
                left += 1
            right += 1
        return longestSubstring + 1
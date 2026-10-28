class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if s1 in s2:
            return True

        s1_chars = {}
        s2_chars = {}
        
        for c in s1:
            s1_chars[c] = s1_chars.get(c, 0) + 1

        left = 0
        s2_chars[s2[left]] = 1
        for right in range(1, len(s2)):
            if right - left + 1 > len(s1):
                s2_chars[s2[left]] -= 1
                if s2_chars[s2[left]] == 0:
                    del s2_chars[s2[left]]
                left += 1
            s2_chars[s2[right]] = s2_chars.get(s2[right], 0) + 1
            if s1_chars == s2_chars:
                return True
            right += 1
        
        return False
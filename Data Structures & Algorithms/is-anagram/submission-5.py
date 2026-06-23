class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = [0] * 26

        for i in range(len(s)):
            chars[ord(s[i])-97] += 1
            chars[ord(t[i])-97] -= 1
        
        if min(chars) == 0 and max(chars) == 0:
            return True
        return False
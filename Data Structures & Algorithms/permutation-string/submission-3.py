class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = {}
        window = {}

        for char in s1:
            target[char] = target.get(char, 0) + 1

        left = 0

        for right in range(len(s2)):
            char = s2[right]
            window[char] = window.get(char, 0) + 1

            # Keep the window at most len(s1) characters long.
            if right - left + 1 > len(s1):
                outgoing = s2[left]
                window[outgoing] -= 1

                if window[outgoing] == 0:
                    del window[outgoing]

                left += 1

            if window == target:
                return True

        return False
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        target = {}
        window = {}

        for c in t:
            target[c] = target.get(c, 0) + 1

        required = len(target)
        formed = 0
        left = 0
        min_window_start = -1
        min_window_end = -1

        for right in range(len(s)):
            c = s[right]

            if c in target:
                window[c] = window.get(c, 0) + 1
                if window[c] == target[c]:
                    formed += 1

            if formed == required:
                # Remove irrelevant characters and surplus copies.
                while s[left] not in target or window[s[left]] > target[s[left]]:
                    if s[left] in target:
                        window[s[left]] -= 1
                    left += 1

                if min_window_start == -1 or right - left < min_window_end - min_window_start:
                    min_window_start = left
                    min_window_end = right

                # Remove a required character to continue searching.
                window[s[left]] -= 1
                formed -= 1
                left += 1

        return s[min_window_start:min_window_end + 1] if min_window_start >= 0 else ""
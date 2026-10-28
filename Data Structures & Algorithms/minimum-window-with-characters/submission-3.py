class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # create dictionary of letters in t
        # go through s -> keep adding a letter until every value in t exists
        if len(t) > len(s):
            return ""

        target = {}
        window = {}

        # populate target
        for c in t:
            target[c] = target.get(c, 0) + 1

        left = 0
        min_window_start = -1
        min_window_end = -1

        def compareTargetAndWindow(target, window):
            for i in target:
                if i not in window:
                    return False
                elif window[i] < target[i]:
                    return False
            return True
        
        for right in range(len(s)):
            # add letter to window frequency
            if s[right] in target:
                window[s[right]] = window.get(s[right], 0) + 1

            # check if letters are fulfilled
            if compareTargetAndWindow(target, window):
                # reduce the left until we hit a letter in target, then note the min window 
                # and then remove the letter to continue checking rest of string
                while s[left] not in target or window[s[left]] > target[s[left]]:
                    if s[left] in window and window[s[left]] > target[s[left]]:
                        window[s[left]] -= 1
                    left += 1

                # if not started: set it, if its shorter: set it, if its longer: dont set it
                if min_window_start == -1 or right - left < min_window_end - min_window_start:
                    min_window_start = left
                    min_window_end = right
                window[s[left]] -= 1
                left += 1

        return s[min_window_start:min_window_end+1] if min_window_start >= 0 else ""
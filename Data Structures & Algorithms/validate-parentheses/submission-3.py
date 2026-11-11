class Solution:
    def isValid(self, s: str) -> bool:
        character_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        char_stack = []
        for char in s:
            if char in character_map:
                char_stack.append(character_map[char])
            elif len(char_stack) == 0 or char != char_stack.pop():
                return False
        return True if len(char_stack) == 0 else False
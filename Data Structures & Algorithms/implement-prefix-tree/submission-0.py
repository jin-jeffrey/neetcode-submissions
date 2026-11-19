class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        current = self.tree
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current["end"] = True

    def search(self, word: str) -> bool:
        current = self.tree
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "end" in current:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.tree
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True
        
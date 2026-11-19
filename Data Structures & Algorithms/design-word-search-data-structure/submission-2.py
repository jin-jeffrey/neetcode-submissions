class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        current = self.words
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current["end"] = True        

    def search(self, word: str) -> bool:
        
        def recursiveSearch(pos, dictionary):
            if pos == len(word):
                if "end" in dictionary:
                    return True
                return False
            if word[pos] == ".":
                exists = False
                for key in dictionary:
                    if key != "end" and recursiveSearch(pos + 1, dictionary[key]):
                        return True
                return exists
            if word[pos] not in dictionary:
                return False
            
            return recursiveSearch(pos + 1, dictionary[word[pos]])

        return recursiveSearch(0, self.words)
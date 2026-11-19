class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["$"] = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(row, col, parent):
            char = board[row][col]
            if char not in parent:
                return

            node = parent[char]

            # A word ends at this trie node.
            word = node.pop("$", None)
            if word:
                result.append(word)

            board[row][col] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and board[nr][nc] != "#"):
                    dfs(nr, nc, node)
            board[row][col] = char

            # This prefix can't lead to any remaining words.
            if not node:
                parent.pop(char)

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie)

        return result
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridLength = 9
        for i in range(gridLength):
            horizontal = set()
            vertical = set()
            square = set()
            for j in range(gridLength):
                # check horizontal and vertical
                if (board[i][j] != "." and board[i][j] in horizontal) or (board[j][i] != "." and board[j][i] in vertical):
                    return False

                horizontal.add(board[i][j])
                vertical.add(board[j][i])
                
                # check square grid
                x = int(j / 3) + 3 * int(i / 3)
                y = int(j % 3 + 3 * (i % 3))
                if board[x][y] != "." and  board[x][y] in square:
                    return False
                square.add(board[x][y])
            horizontal = set()
            vertical = set()
            square = set()
        return True
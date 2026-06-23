class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridLength = 9
        # check horizontal and horizontal
        for i in range(gridLength):
            horizontal = set()
            vertical = set()
            square = set()
            for j in range(gridLength):
                if (board[i][j] != "." and board[i][j] in horizontal) or (board[j][i] != "." and board[j][i] in vertical):
                    print(board[i][j], board[j][j],  horizontal, vertical, board[i][j] in horizontal, board[j][i] in vertical)
                    return False

                horizontal.add(board[i][j])
                vertical.add(board[j][i])
                
                # check grid
                x = int(j / 3) + 3 * int(i / 3)
                y = int(j % 3 + 3 * (i % 3))
                print(x,y)
                if board[x][y] != "." and  board[x][y] in square:
                    print("square", board[x][y], square, (x,y), (i,j))
                    return False
                square.add(board[x][y])
                #print(square)
            horizontal = set()
            vertical = set()
            square = set()
        return True
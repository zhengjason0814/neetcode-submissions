class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        squares = defaultdict(set)

        for currRow in range(9):
            for currColumn in range(9):
                if (board[currRow][currColumn] == "."):
                    continue
                if (board[currRow][currColumn] in row[currRow] or
                    board[currRow][currColumn] in column[currColumn] or
                    board[currRow][currColumn] in squares[(currRow // 3, currColumn // 3)]):
                    return False
                row[currRow].add(board[currRow][currColumn])
                column[currColumn].add(board[currRow][currColumn])
                squares[(currRow // 3, currColumn // 3)].add(board[currRow][currColumn])
            
        return True
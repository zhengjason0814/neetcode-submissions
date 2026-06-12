class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = defaultdict(set)
        columnDict = defaultdict(set)
        squareDict = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowDict[r] or
                    board[r][c] in columnDict[c] or
                    board[r][c] in squareDict[(r // 3, c // 3)]):
                    return False
                rowDict[r].add(board[r][c])
                columnDict[c].add(board[r][c])
                squareDict[(r // 3, c // 3)].add(board[r][c])

        return True
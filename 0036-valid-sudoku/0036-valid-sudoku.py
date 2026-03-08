class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    num = board[i][j]
                    if (f"{i}R{num}" in s or f"{j}C{num}" in s or f"{i//3}R{num}{j//3}C{num}" in s):
                        return False

                    s.add(f"{i}R{num}")
                    s.add(f"{j}C{num}")
                    s.add(f"{i//3}R{num}{j//3}C{num}")
        return True
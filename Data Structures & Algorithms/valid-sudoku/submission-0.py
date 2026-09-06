class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashr = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in hashr:
                        hashr.add(board[i][j])
                    else:
                        return False
                else:
                    continue
            hashr.clear()

        hashc = set()
        for i in range(9):
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] not in hashc:
                        hashc.add(board[j][i])
                    else:
                        return False
                else:
                    continue
            hashc.clear()

        hashsub = set()

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                hashsub.clear()
                for r in range(3):
                    for c in range(3):
                        actual_row = box_row + r
                        actual_col = box_col + c
                        if board[actual_row][actual_col] != ".":
                            if board[actual_row][actual_col] not in hashsub:
                                hashsub.add(board[actual_row][actual_col])
                            else:
                                return False
                        else:
                            continue

        return True

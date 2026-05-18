class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def val_row(row, board) -> bool:
            nums = [1 for _ in range(9)]
            for i in range(9):
                num = board[row][i]
                if num == '.': continue
                if nums[int(num)-1] != 1:
                    return False
                nums[int(num)-1] -= 1
            return True

        def val_col(col, board) -> bool:
            nums = [1 for _ in range(9)]
            for i in range(9):
                num = board[i][col]
                if num == '.': continue
                if nums[int(num)-1] != 1:
                    return False
                nums[int(num)-1] -= 1
            return True

        def val_group(r,c,board) -> bool:
            nums = [1 for _ in range(9)]
            for i in range(3):
                for j in range(3):
                    num = board[r+i][c+j]
                    if num == '.': continue
                    if nums[int(num)-1] != 1:
                        return False
                    nums[int(num)-1] -= 1
            return True

        for i in range(9):
            if not (val_row(i, board) and val_col(i, board)):
                return False

        for i in range(3):
            for j in range(3):
                if not val_group(i*3, j*3, board):
                    return False

        return True
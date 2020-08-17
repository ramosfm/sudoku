

class Sudoku:

    def __init__(self):
        self.size = 9

    def check_grids(self, board):
        # Check grids
        grid = 0
        row = 0
        col = 0
        while grid < self.size:
            if (grid != 0) and ((grid % 3) == 0):
                row += 1
                col = 0
            b = []
            for i in range(row * 3, (row * 3) + 3):
                for j in range(col * 3, (col * 3) + 3):
                    b.append(board[i][j])
            # Check Grid duplicated
            if self.duplicated(b):
                return True
            col += 1
            grid += 1
        return False

    def duplicated(self, row):
        s = set()
        for r in row:
            if r in s:
                return True
            else:
                s.add(r)
        return False

    def zero_validate(self, row):
        for r in row:
            if r == 0:
                return True
        return False

    def valid_solution(self, board):

        for row in board:
            # Check zero
            if self.zero_validate(row):
                return False
            # Check row duplicated
            if self.duplicated(row):
                return False

        # Check column

        col = 0
        while col < self.size:
            c = []
            for row in range(self.size):
                c.append(board[row][col])
            # Check Col duplicated
            if self.duplicated(c):
                return False
            col += 1

        if self.check_grids(board):
            return False

        return True


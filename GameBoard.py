import numpy as np;

class Connect4Board:
    #0 is empty, -1 is black, 1 is red
    def __init__(self, rows=6, columns=7, board = None):
        self.rows = rows
        self.columns = columns
        if board is None:
            self.board = np.zeros(shape=(rows,columns))
        else:
            self.board = np.copy(board)
    def get_lowest_unfilled_slot(self, col):
        '''returns the row in a particular column that is unfilled'''
        for i in range(0,self.rows):
            if self.board[i][col] == 0:
                return i
        return None
    def get_possible_moves(self):
        open_cols = []
        for i in range(0,self.columns):
            if self.get_lowest_unfilled_slot(i) is not None:
                open_cols.append(i)
        return open_cols
    '''makes a move and returns a new GameBoard object that represents the board position after the move'''
    def make_move(self, column, color):
        x = self.get_lowest_unfilled_slot(column)
        if x is not None:
            new_board = Connect4Board(board=self.board)
            new_board.board[x][column] = color
            return new_board

    def check_four_in_a_row(self):
        horizontal_indices_list = []
        vertical_indices_list = []
        diagonal_indices_list = []
        for i in range(0,self.columns):
            for j in range(0, self.rows):
                if j+3 < self.rows:
                    vertical_indices_list.append([(i,j),(i,j+1),(i,j+2),(i,j+3)])
                if i+3 < self.columns:
                    horizontal_indices_list.append([(i,j),(i+1,j),(i+2,j),(i+3,j)])
                if i+3 <self.columns and j+3 < self.columns:
                    diagonal_indices_list.append([(i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3)])
                if i+3 <self.columns and j-3 >= 0:
                    diagonal_indices_list.append([(i,j),(i+1,j-1),(i+2,j-2),(i+3,j-3)])
        for four_row in horizontal_indices_list:
            if (self.board[four_row] == np.ones(4)).all():
                return self.board[four_row][0];
        for four_row in vertical_indices_list:
            if (self.board[four_row] == np.ones(4)).all():
                return self.board[four_row][0];
        for four_row in diagonal_indices_list:
            if (self.board[four_row] == np.ones(4)).all():
                return self.board[four_row][0];
        return None
    def print_board(self):
        print(np.flip(self.board,0))



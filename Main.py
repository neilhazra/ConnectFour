import GameBoard as gb

x = gb.Connect4Board()
x.make_move(0,1).make_move(0,-1).print_board()

class TreeSolver:
    def __init__(self, depth = 10):
        self.children = []

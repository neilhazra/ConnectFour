import Solver as sv
import GameBoard as gb

x = sv.TreeSolver(gb.Connect4Board(), 1)
sv.propagate(x, 3)
x,y = sv.minimax(x)

a,b = x.currentBoard.lastMove

i = 3 #sets the skill level

while True:
    i += 2
    sv.propagate(x, i)
    print("I moved!")
    x.currentBoard.print_board()
    move = input("Make your move")
    x = sv.find_child_node_representing_move(x, int(move))
    x.currentBoard.print_board()
    print("I am thinking")
    if x.currentBoard.check_four_in_a_row() == -1:
        print("You Won!")
    x, y = sv.minimax(x)
    a, b = x.currentBoard.lastMove
    if x.currentBoard.check_four_in_a_row() == 1:
        print("I Won!")
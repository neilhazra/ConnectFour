import Solver as sv
import GameBoard as gb



x = sv.TreeSolver(gb.Connect4Board(), 1)
sv.propagate(x, 3)
x,y = sv.minimax(x)

a,b = x.currentBoard.lastMove

i = 4 #sets the skill level

while True:
    i += 2
    sv.propagate(x, i)
    print("I moved!")
    #Add code here to display board
    #i.e graphics.displayBoard(x.currentBoard)
    x.currentBoard.print_board()
    #Add code to determine their move i.e mouse click
    move = input("Make your move")
    x = sv.find_child_node_representing_move(x, int(move))
    #Add code here to display board
    #i.e graphics.displayBoard(x.currentBoard)
    x.currentBoard.print_board()
    print("I am thinking")
    if x.currentBoard.check_four_in_a_row() == -1:
        print("You Won!")
        break
    x, y = sv.minimax(x)
    a, b = x.currentBoard.lastMove
    if x.currentBoard.check_four_in_a_row() == 1:
        print("I Won!")
        break
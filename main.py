import Solver as sv
import GameBoard as gb
import pickle as pk

i = 3 #sets the skill level
x = sv.TreeSolver(gb.Connect4Board(), 1)
sv.propagate(x, 3)


x,y = sv.minimax(x)
x.currentBoard.print_board()

while True:
    i+= 2
    #Add code to determine their move i.e mouse click
    move = input("Make your move")
    x = sv.find_child_node_representing_move(x, int(move))
    #Add code here to display board
    #i.e graphics.displayBoard(x.currentBoard)
    x.currentBoard.print_board()
    if x.currentBoard.check_four_in_a_row() == -1:
        print("You Won!")
        break

    print("I am thinking")

    sv.propagate(x, i)
    x, y = sv.minimax(x)

    print("I moved!")
    # Add code here to display board
    # i.e graphics.displayBoard(x.currentBoard)
    x.currentBoard.print_board()#Add code here to display board
    if x.currentBoard.check_four_in_a_row() == 1:
        print("I Won!")
        break
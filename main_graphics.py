from tkinter import *
import Solver as sv
import GameBoard as gb
import numpy as np

try:
    i = int(input("Please type in a skill level from 1 to 4. 3 is recommended")) #sets the skill level
except:
    print("Continuing with default value of 3")
    i = 3
x = sv.TreeSolver(gb.Connect4Board(), 1)
sv.propagate(x, i)

x,y = sv.minimax(x)


def make_move(move):
    print(move)
    global i, x, root
    i += 2
    x = sv.find_child_node_representing_move(x, int(move))
    update_board()
    root.update()
    if x.currentBoard.check_four_in_a_row() == -1:
        print("You Won!")
        quit()

    print("I'm thinking... Be patient")
    sv.propagate(x, i)
    x, y = sv.minimax(x)
    print("I moved! Score = " + str(y))
    update_board()
    if x.currentBoard.check_four_in_a_row() == 1:
        print("I Won!")
        quit()

root = Tk()
rows = list()
for r in range(x.currentBoard.rows):
    row = list()
    r_frame = Frame(root)
    r_frame.pack()
    for c in range(x.currentBoard.columns):
        cell = Button(r_frame, width=10, height=5, borderwidth=1, relief='solid', command=lambda curr=c: make_move(curr))
        cell.pack(side=LEFT)
        row.append(cell)
    rows.append(row)

color_map = {0:'white', -1:'black', 1:'red'}
def update_board():
    b = np.flip(x.currentBoard.board, 0)
    for r in range(0, b.shape[0]):
        for c in range(0, b.shape[1]):
            rows[r][c].configure(bg=color_map[b[r][c]])
update_board()



mainloop()

import GameBoard as gb

class TreeSolver:
    def __init__(self, currentBoard, depth = 0):
        self.depth = depth
        self.currentBoard = currentBoard
        self.children = []
    def loss(self, color):
        return self.currentBoard.score_player(color)-self.currentBoard.score_player(-color);
    def isLeaf(self):
        return len(self.children) == 0
    def apply_all_moves(self):
        if not len(self.children) == self.currentBoard.get_possible_moves():
            for move in self.currentBoard.get_possible_moves():
                self.children.append(TreeSolver(self.currentBoard.make_move(move), depth=self.depth-1))
def find_child_node_representing_move(node, move):
    for child in node.children:
        if child.currentBoard.lastMove[1] == move:
            return child

def minimax(node):
    if node.isLeaf():
        return (None,node.loss(1))
    if node.currentBoard.whoseMove == 1:
        return maximize_children(node)
    else:
        return minimize_children(node)


def minimize_children(node):
    min = 1000000000000 # arbitrarily big number
    min_child_node = None
    for child in node.children:
        _,temp = minimax(child)
        if temp < min:
            min = temp
            min_child_node = child
    return (min_child_node, min)

def maximize_children(node):
    max = -100000000000
    max_child_node = None
    for child in node.children:
        _,temp = minimax(child)
        if temp > max:
            max = temp
            max_child_node = child
    return (max_child_node, max)


def propagate_helper(node, depth):
    for child_node in node.children:
        if child_node.depth == -depth:
            return
        child_node.apply_all_moves()
        propagate_helper(child_node, depth)

def propagate(node, depth):
    node.apply_all_moves()
    propagate_helper(node, depth)



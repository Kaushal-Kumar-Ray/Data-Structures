class GameNode:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.children = []

    def generate_moves(self):
        for i in range(9):
            if self.board[i] == " ":
                new_board = self.board[:i] + self.player + self.board[i+1:]
                next_player = "O" if self.player == "X" else "X"
                child = GameNode(new_board, next_player)
                self.children.append(child)

    def print_tree(self, depth=0):
        print(" " * depth * 2 + self.board)
        for child in self.children:
            child.print_tree(depth + 1)

# Starting empty board
root = GameNode("         ", "X")
root.generate_moves()
root.print_tree()

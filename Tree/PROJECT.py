class ChessNode:
    """
    A node in the chess game tree.
    Each node represents a board state and has children representing possible moves.
    """
    def __init__(self, board=None, parent=None, move=None, depth=0):
        self.board = board  # Chess board state
        self.parent = parent  # Parent node
        self.children = []    # Child nodes (possible moves)
        self.move = move      # Move that led to this state
        self.depth = depth    # Depth in tree
        self.value = None     # Evaluation value
    
    def add_child(self, child_node):
        """Add a child node representing a possible move."""
        self.children.append(child_node)
    
    def generate_children(self, depth_limit=1):
        """Generate all valid moves as child nodes up to depth_limit."""
        if self.depth >= depth_limit:
            return
        
        # Get all valid moves for current player
        valid_moves = self.board.get_valid_moves()
        
        for move in valid_moves:
            # Create a new board with the move applied
            new_board = self.board.copy()
            new_board.make_move(move)
            
            # Create a child node with the new board state
            child = ChessNode(
                board=new_board,
                parent=self,
                move=move,
                depth=self.depth + 1
            )
            
            # Add the child to the current node
            self.add_child(child)
            
            # Recursively generate children for this node
            child.generate_children(depth_limit)


class ChessPiece:
    """Base class for chess pieces."""
    def __init__(self, color):
        self.color = color  # 'white' or 'black'
        self.has_moved = False
    
    def get_valid_moves(self, board, position):
        """Get all valid moves for this piece at given position."""
        pass
    
    def __str__(self):
        return self.symbol


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P' if color == 'white' else 'p'
    
    def get_valid_moves(self, board, position):
        row, col = position
        moves = []
        direction = -1 if self.color == 'white' else 1
        
        # Forward move
        if 0 <= row + direction < 8 and board.board[row + direction][col] is None:
            moves.append((row + direction, col))
            
            # Double move from starting position
            if (self.color == 'white' and row == 6) or (self.color == 'black' and row == 1):
                if (0 <= row + 2*direction < 8 and 
                    board.board[row + 2*direction][col] is None):
                    moves.append((row + 2*direction, col))
        
        # Capture moves
        for c_offset in [-1, 1]:
            if 0 <= row + direction < 8 and 0 <= col + c_offset < 8:
                target = board.board[row + direction][col + c_offset]
                if target is not None and target.color != self.color:
                    moves.append((row + direction, col + c_offset))
        
        return moves


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R' if color == 'white' else 'r'
    
    def get_valid_moves(self, board, position):
        row, col = position
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = board.board[r][c]
                if target is None:
                    moves.append((r, c))
                else:
                    if target.color != self.color:
                        moves.append((r, c))
                    break
                r, c = r + dr, c + dc
        
        return moves


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'N' if color == 'white' else 'n'
    
    def get_valid_moves(self, board, position):
        row, col = position
        moves = []
        offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for dr, dc in offsets:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board.board[r][c]
                if target is None or target.color != self.color:
                    moves.append((r, c))
        
        return moves


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B' if color == 'white' else 'b'
    
    def get_valid_moves(self, board, position):
        row, col = position
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonals
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = board.board[r][c]
                if target is None:
                    moves.append((r, c))
                else:
                    if target.color != self.color:
                        moves.append((r, c))
                    break
                r, c = r + dr, c + dc
        
        return moves


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q' if color == 'white' else 'q'
    
    def get_valid_moves(self, board, position):
        # Queen combines Rook and Bishop moves
        rook = Rook(self.color)
        bishop = Bishop(self.color)
        
        rook_moves = rook.get_valid_moves(board, position)
        bishop_moves = bishop.get_valid_moves(board, position)
        
        return rook_moves + bishop_moves


class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K' if color == 'white' else 'k'
    
    def get_valid_moves(self, board, position):
        row, col = position
        moves = []
        
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8:
                    target = board.board[r][c]
                    if target is None or target.color != self.color:
                        # TODO: Check if move puts king in check
                        moves.append((r, c))
        
        # TODO: Castling logic
        
        return moves


class ChessBoard:
    """Represents a chess board and its state."""
    def __init__(self):
        # Initialize an 8x8 board
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.current_player = 'white'
        self.setup_board()
        self.move_history = []
    
    def setup_board(self):
        """Set up the initial chess board position."""
        # Place pawns
        for col in range(8):
            self.board[1][col] = Pawn('black')
            self.board[6][col] = Pawn('white')
        
        # Place rooks
        self.board[0][0] = Rook('black')
        self.board[0][7] = Rook('black')
        self.board[7][0] = Rook('white')
        self.board[7][7] = Rook('white')
        
        # Place knights
        self.board[0][1] = Knight('black')
        self.board[0][6] = Knight('black')
        self.board[7][1] = Knight('white')
        self.board[7][6] = Knight('white')
        
        # Place bishops
        self.board[0][2] = Bishop('black')
        self.board[0][5] = Bishop('black')
        self.board[7][2] = Bishop('white')
        self.board[7][5] = Bishop('white')
        
        # Place queens
        self.board[0][3] = Queen('black')
        self.board[7][3] = Queen('white')
        
        # Place kings
        self.board[0][4] = King('black')
        self.board[7][4] = King('white')
    
    def copy(self):
        """Create a deep copy of the current board state."""
        new_board = ChessBoard()
        new_board.board = [[None for _ in range(8)] for _ in range(8)]
        
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None:
                    # Create a new piece of the same type
                    if isinstance(piece, Pawn):
                        new_piece = Pawn(piece.color)
                    elif isinstance(piece, Rook):
                        new_piece = Rook(piece.color)
                    elif isinstance(piece, Knight):
                        new_piece = Knight(piece.color)
                    elif isinstance(piece, Bishop):
                        new_piece = Bishop(piece.color)
                    elif isinstance(piece, Queen):
                        new_piece = Queen(piece.color)
                    elif isinstance(piece, King):
                        new_piece = King(piece.color)
                    
                    new_piece.has_moved = piece.has_moved
                    new_board.board[row][col] = new_piece
        
        new_board.current_player = self.current_player
        new_board.move_history = self.move_history.copy()
        
        return new_board
    
    def make_move(self, move):
        """
        Make a move on the board.
        move is a tuple ((from_row, from_col), (to_row, to_col))
        """
        (from_row, from_col), (to_row, to_col) = move
        piece = self.board[from_row][from_col]
        
        # Update piece position
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        
        # Mark the piece as moved
        piece.has_moved = True
        
        # Record the move
        self.move_history.append(move)
        
        # Switch current player
        self.current_player = 'black' if self.current_player == 'white' else 'white'
    
    def get_valid_moves(self):
        """Get all valid moves for the current player."""
        valid_moves = []
        
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == self.current_player:
                    # Get valid moves for this piece
                    piece_moves = piece.get_valid_moves(self, (row, col))
                    # Add source position to each move
                    for dest in piece_moves:
                        valid_moves.append(((row, col), dest))
        
        return valid_moves
    
    def is_in_check(self, color):
        """Determine if the given color's king is in check."""
        # Find the king's position
        king_pos = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if (piece is not None and 
                    isinstance(piece, King) and 
                    piece.color == color):
                    king_pos = (row, col)
                    break
            if king_pos:
                break
        
        # If king not found, something is wrong
        if not king_pos:
            return False
        
        # Check if any opponent's piece can capture the king
        opponent_color = 'black' if color == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == opponent_color:
                    moves = piece.get_valid_moves(self, (row, col))
                    if king_pos in moves:
                        return True
        
        return False
    
    def is_checkmate(self):
        """Determine if the current player is in checkmate."""
        if not self.is_in_check(self.current_player):
            return False
        
        # Check if any move can get out of check
        valid_moves = self.get_valid_moves()
        for move in valid_moves:
            new_board = self.copy()
            new_board.make_move(move)
            if not new_board.is_in_check(self.current_player):
                return False
        
        return True
    
    def algebraic_to_coords(self, algebraic):
        """Convert algebraic notation (e.g., 'e4') to board coordinates (row, col)."""
        if len(algebraic) != 2:
            return None
        
        col = ord(algebraic[0].lower()) - ord('a')
        row = 8 - int(algebraic[1])
        
        if 0 <= row < 8 and 0 <= col < 8:
            return (row, col)
        return None
    
    def coords_to_algebraic(self, coords):
        """Convert board coordinates (row, col) to algebraic notation."""
        row, col = coords
        return f"{chr(col + ord('a'))}{8 - row}"
    
    def __str__(self):
        """Return a string representation of the board."""
        s = "  a b c d e f g h\n"
        for row in range(8):
            s += f"{8 - row} "
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    s += piece.symbol + " "
                else:
                    s += ". "
            s += f"{8 - row}\n"
        s += "  a b c d e f g h"
        return s


class ChessGame:
    """Main chess game class that manages the game flow."""
    def __init__(self):
        self.board = ChessBoard()
        self.root_node = ChessNode(board=self.board)
        
    def build_move_tree(self, depth=2):
        """Build a tree of possible moves up to the given depth."""
        self.root_node = ChessNode(board=self.board)
        self.root_node.generate_children(depth)
        return self.root_node
    
    def print_board(self):
        """Print the current board state."""
        print(self.board)
    
    def play_move(self, from_pos, to_pos):
        """Play a move using algebraic or coordinate notation."""
        # Convert algebraic notation to coordinates if needed
        if isinstance(from_pos, str):
            from_pos = self.board.algebraic_to_coords(from_pos)
        if isinstance(to_pos, str):
            to_pos = self.board.algebraic_to_coords(to_pos)
        
        # Validate the positions
        if not from_pos or not to_pos:
            print("Invalid position")
            return False
        
        # Check if there's a piece at the from position
        piece = self.board.board[from_pos[0]][from_pos[1]]
        if not piece:
            print("No piece at the source position")
            return False
        
        # Check if it's the current player's piece
        if piece.color != self.board.current_player:
            print(f"It's {self.board.current_player}'s turn")
            return False
        
        # Check if the move is valid
        valid_moves = piece.get_valid_moves(self.board, from_pos)
        if to_pos not in valid_moves:
            print("Invalid move for this piece")
            return False
        
        # Make the move
        self.board.make_move((from_pos, to_pos))
        
        # Update the game tree
        self.build_move_tree()
        
        return True
    
    def play_game(self):
        """Start an interactive chess game."""
        print("Chess Game")
        print("Enter moves in the format 'e2 e4' (from to)")
        print("Type 'quit' to exit")
        
        while True:
            self.print_board()
            print(f"\n{self.board.current_player.capitalize()}'s turn")
            
            # Check for checkmate or stalemate
            if self.board.is_checkmate():
                winner = "Black" if self.board.current_player == "white" else "White"
                print(f"Checkmate! {winner} wins!")
                break
            
            if self.board.is_in_check(self.board.current_player):
                print(f"{self.board.current_player.capitalize()} is in check!")
            
            # Get player input
            move_input = input("Enter your move: ")
            if move_input.lower() == 'quit':
                break
            
            try:
                from_pos, to_pos = move_input.split()
                if not self.play_move(from_pos, to_pos):
                    print("Invalid move, try again")
            except ValueError:
                print("Invalid input format. Use 'e2 e4' format.")


# Example usage
if __name__ == "__main__":
    game = ChessGame()
    game.play_game()
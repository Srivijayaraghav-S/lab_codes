class TicTacToeMinimax:
    def __init__(self):
        """Initialize the Tic Tac Toe game."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Human player
        self.computer = 'O'       # Computer player
    def display_board(self):
        """Display the current board."""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    def make_move(self, row, col, player):
        """Make a move for a given player."""
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False
    def check_win(self, player):
        """Check if the given player has won."""
        for i in range(3):
            if all([cell == player for cell in self.board[i]]) or \
               all([self.board[j][i] == player for j in range(3)]):
                return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False
    def is_draw(self):
        """Check if the game is a draw."""
        return all(cell != ' ' for row in self.board for cell in row)
    def minimax(self, alpha, beta, maximizing_player):
        """Minimax algorithm with Alpha-Beta pruning to determine the best move."""
        if self.check_win(self.computer):
            return 1
        if self.check_win(self.current_player):
            return -1
        if self.is_draw():
            return 0
        if maximizing_player:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.computer
                        eval = self.minimax(alpha, beta, False)
                        self.board[i][j] = ' '
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.current_player
                        eval = self.minimax(alpha, beta, True)
                        self.board[i][j] = ' '
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval
    def find_best_move(self):
        """Find the best move for the computer using Minimax."""
        best_move = (-1, -1)
        best_value = float('-inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.computer
                    move_value = self.minimax(float('-inf'), float('inf'), False)
                    self.board[i][j] = ' '
                    if move_value > best_value:
                        best_move = (i, j)
                        best_value = move_value
        return best_move
    def play(self):
        """Main game loop."""
        while True:
            self.display_board()
            if self.is_draw():
                print("It's a draw!")
                return
            # Human's move
            if not self.check_win(self.computer):
                row, col = map(int, input(f"Player {self.current_player}, enter your move (row col): ").split())
                if not self.make_move(row, col, self.current_player):
                    print("Invalid move!")
                    continue
                if self.check_win(self.current_player):
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    return
            # Computer's move
            if not self.check_win(self.current_player) and not self.is_draw():
                print("Computer's move:")
                row, col = self.find_best_move()
                self.make_move(row, col, self.computer)
                if self.check_win(self.computer):
                    self.display_board()
                    print(f"Player {self.computer} wins!")
                    return
game = TicTacToeMinimax()
game.play()
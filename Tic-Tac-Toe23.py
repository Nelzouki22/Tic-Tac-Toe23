import random

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Initialize the game board with empty spaces
        self.current_player = random.choice(['X', 'O'])  # Randomly select the starting player

    def display_board(self):
        # Display the current state of the game board
        for row in range(0, 9, 3):
            print(f"{self.board[row]} | {self.board[row + 1]} | {self.board[row + 2]}")
            if row < 6:
                print("-" * 9)

    def make_move(self, position):
        # Check if the move is valid and update the game board
        if 1 <= position <= 9 and self.board[position - 1] == " ":
            self.board[position - 1] = self.current_player
            return True
        return False

    def check_winner(self):
        # Check for a winning state (3 in a row)
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True

        return False

    def check_draw(self):
        # Check for a draw (all positions are filled)
        return " " not in self.board

    def switch_player(self):
        # Switch to the other player for the next turn
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Player 1: X, Player 2: O")
        print("To make a move, enter the number of the position (1-9) as shown below:")
        print("1 | 2 | 3")
        print("4 | 5 | 6")
        print("7 | 8 | 9")

        while True:
            self.display_board()

            position = int(input(f"Player {self.current_player}, enter your move (1-9): "))

            if self.make_move(position):
                if self.check_winner():
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    break
                elif self.check_draw():
                    self.display_board()
                    print("It's a draw!")
                    break
                self.switch_player()
            else:
                print("Invalid move. Try again.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()

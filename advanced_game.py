#! python 3.12
import random, argparse

# Tic Tac Toe Game with AI
# This is a simple implementation of Tic Tac Toe where the player can play against an AI.

# we use a nested list to represent the board
# in which each cell can be 0 (empty), 1 (player), or -1 (AI)
# but when we print the board, we will use ' ' for empty, 'X' for player, and 'O' for AI
def print_cell(value):
    if value == 0:
        return ' '
    elif value == 1:
        return 'X'
    elif value == -1:
        return 'O'

def create_board():
    return [[0 for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("Current board:")
    for row in board:
        print("|".join(print_cell(cell) for cell in row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if abs(sum(board[i])) == 3:  # Check rows
            return board[i][0]
        if abs(sum(board[j][i] for j in range(3))) == 3:  # Check columns
            return board[0][i]

    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:  # Check main diagonal
        return board[0][0]
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:  # Check anti-diagonal
        return board[0][2]

    return 0  # No winner yet

def is_board_full(board):
    return all(cell != 0 for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def random_ai_move(board):
    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return None

    # AI chooses a random empty cell
    i, j = random.choice(empty_cells)
    board[i][j] = -1  # AI marks its move
    return i, j

def advanced_ai_move(board):
    # This function implements a simple AI that tries to win or block the player
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # Check if the cell is empty
                # Try to place AI's mark and check for a win
                board[i][j] = -1
                if check_winner(board) == -1:
                    return i, j  # AI wins
                board[i][j] = 0  # Reset the cell

    # Block player's winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  # Check if the cell is empty
                board[i][j] = 1
                if check_winner(board) == 1:
                    board[i][j] = -1  # Block player's move
                    return i, j
                board[i][j] = 0  # Reset the cell

    return random_ai_move(board)  # If no immediate win or block, choose randomly

def player_move(board):
    while True:
        try:
            move = input("Enter your move (row and column, e.g., 1 2): ")
            i, j = map(int, move.split())
            if board[i][j] == 0:  # Check if the cell is empty
                board[i][j] = 1  # Player marks its move
                return i, j
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")

def main():
    parser = argparse.ArgumentParser(description="Play Tic Tac Toe against an AI.")
    parser.add_argument("--ai", action="store_true", help="Use advanced AI instead of random AI")
    board = create_board()
    print_board(board)
    if parser.parse_args().ai:
        ai_move = advanced_ai_move
        print("Playing against advanced AI.")
    else:
        ai_move = random_ai_move
        print("Playing against random AI.")
    print("Welcome to Tic Tac Toe!")
    print("You are 'X' and the AI is 'O'.")
    while True:
        # Player's turn
        player_move(board)
        print_board(board)
        if check_winner(board) == 1:
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI's turn
        ai_move(board)
        print_board(board)
        if check_winner(board) == -1:
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
    print("Game over!")
if __name__ == "__main__":
    main()
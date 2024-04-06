def create_board():
    return [[" " for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    for row in board:
        if " ".join(row).count(player * 4) > 0:
            return True

    for col in range(7):
        if "".join(board[row][col] for row in range(6)).count(player * 4) > 0:
            return True

    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    for row in range(3):
        for col in range(3, 7):
            if all(board[row + i][col - i] == player for i in range(4)):
                return True

    return False

def play_connect_four():
    board = create_board()
    current_player = "X"

    print("Welcome to Connect Four!")
    print_board(board)

    for _ in range(42):
        col = int(input(f"Player {current_player}, choose a column (1-7): ")) - 1

        for row in range(5, -1, -1):
            if board[row][col] == " ":
                board[row][col] = current_player
                break
        else:
            print("Column is full. Try again.")
            continue

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        current_player = "O" if current_player == "X" else "X"
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_connect_four()

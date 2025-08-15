board = [" " for _ in range(9)]

# Ask for player names
player_X_name = input("Enter name for Player X: ")
player_O_name = input("Enter name for Player O: ")


# printing the board
def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


# check for a win
def check_win(player):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # rows
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # columns
        [0, 4, 8],
        [2, 4, 6],  # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


# Main game loop
player = "X"
for turn in range(9):
    print_board()
    # what is the players name
    current_name = player_X_name if player == "X" else player_O_name

    # make sure move is okay
    while True:
        try:
            move = int(input(f"{current_name} ({player}), choose a spot 1-9: ")) - 1
            if move < 0 or move > 8:
                print("Number must be between 1 and 9. Try again.")
            elif board[move] != " ":
                print("Spot already taken! Try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Enter a number 1-9.")

    board[move] = player

    if check_win(player):
        print_board()
        print(f"{current_name} ({player}) wins!")
        break

    # Switch player
    player = "O" if player == "X" else "X"
else:
    print_board()
    print("It's a tie!")

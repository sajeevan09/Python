
# prints current state of the board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Check if the current player has won the game
def check_winner(board, mark):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for cond in win_conditions:
        if all(board[i] == mark for i in cond):
            return True
    return False

# Function to run the game
def tic_tac_toe():
    board = [' '] * 9
    current_player = "X"
    moves = 0

    print("Welcome to Tic Tac Toe!")
    # Shows postions of board
    print_board(['1','2','3','4','5','6','7','8','9'])

    while moves < 9:
        print_board(board)
        # Ask the current player to choose a spot
        try:
            move = int(input(f"Player {current_player}, choose a spot (1-9): ")) - 1
        except ValueError:
            print(" Invalid input. Please enter a number 1-9.")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print(" That spot is taken or invalid. Try again.")
            continue

        # Place the players mark on the board
        board[move] = current_player
        moves += 1

        # Check if current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f" Player {current_player} wins!")
            return
    
        # Switch turns
        current_player = "O" if current_player == "X" else "X"

    # If the loop ends without a winner, it's a tie
    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
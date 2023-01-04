def print_board(entries):
    line = "+---+---+---+"
    output = line
    n = 0
    for entry in entries:
        if n % 3 == 0:
            output = output + "\n| "
        else:
            output = output + " | "
        output = output + str(entry)
        if n % 3 == 2:
            output = output + " |\n"
            output = output + line
        n = n + 1
    print(output)
    print()


def game_over(board, current_player):
    print_board(board)
    print("GAME OVER")
    print(current_player, "has won")
    exit()

def top_row_is_winner(board):
    if board[0] == board[1] and board[1] == board[2]:
        return True

def middle_row_winner(board):
    if board[3] == board[4] and board[4] == board[5]:
        return True

def bottom_row_winner(board):
    if board[6] == board[7] and board[7] == board[8]:
        return True

def left_vert_win(board):
    if board[0] == board[3] and board[3] == board[6]:
        return True

def center_vert_win(board):
    if board[1] == board[4] and board[4] == board[7]:
        return True

def right_vert_win(board):
    if board[0] == board[4] and board[4] == board[8]:
        return True

def diag_left_right_win(board):
    if board[0] == board[4] and board[4] == board[8]:
        return True

def diag_right_left_win(board):
    if board[2] == board[4] and board[4] == board[6]:
        return True


board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if top_row_is_winner(board):
        game_over(board, current_player)
    elif middle_row_winner(board):
        game_over(board, current_player)
    elif bottom_row_winner(board):
        game_over(board, current_player)
    elif left_vert_win(board):
       game_over(board, current_player)
    elif center_vert_win(board):
        game_over(board, current_player)
    elif right_vert_win(board):
        game_over(board, current_player)
    elif diag_left_right_win(board):
        game_over(board, current_player)
    elif diag_right_left_win(board):
        game_over(board, current_player)

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")

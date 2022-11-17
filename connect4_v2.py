LOG = False
def log(value):
    if LOG: print(value)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
UP_RIGHT = (1, -1)
DOWN_LEFT = (-1, 1)
UP_LEFT = (-1, -1)
DOWN_RIGHT = (1, 1)

def create_board(rows, columns):
    log(rows)
    log(columns)
    print("Creating a board with " + str(rows) + " rows and " + str(columns) + " columns.\n")
    board = []
    for col in range(columns):
        board.append([" "] * rows)
    log(board)
    return board

#Asks for user input, passes it to check_input, gives and error message and loops if the input is not in desired range.
def choose_row():
    rows = input("Choose the number of rows in your board (min 4, max 10): ")
    log("User inputted " + rows + " rows.")
    if check_in_range(rows) == False:
        choose_row()
    else:
        return rows

#Asks for user input, passes it to check_input, gives an error message and loops if the input is not in desired range.
def choose_col():
    columns = input("Now choose the number of columns in your board (min 4, max 10): ")
    log("User inputted " + columns + " columns.")
    if check_in_range(columns) == False:
        choose_col()
    else:
        return columns

#This function checks if the user input is an integer and is in the min/ max board range
def check_in_range(user_input):
    try:
        num = int(user_input)
    except ValueError:
        print("That is not a number between 4 and 10!")
        return False
    else:
        if num in [4, 5, 6, 7, 8, 9, 10]:
            return True
        else:
            print("That is not a number between 4 and 10!")
            return False

# This code prints my board with added bells and whistles but most importantly passing my 2D array to the correct places.
def print_board(board):
    header = ''
    for num in range(1, len(board) + 1):
        header += '  ' + str(num) + ' '
    print(header)
    print("+---" * len(board) + '+')
    for row in range(len(board[0])):
        print('|   ' * len(board) + '|')   

        row_with_items = ''
        for col in range(len(board)):
            row_with_items += ('| ' + str(board[col][row]) + ' ')
        print(row_with_items + '|')

        print('|   ' * len(board) + '|') 
        print("+---" * len(board) + '+')
    print(header)
    print("\n")

# Function asks player 1 to choose X or O, checks that the input matches the accepted game pieces (printing an error if not and looping), assigns the choice to variable player1_piece (correcting for lowercase input) and automatically assigns the remaining piece to player2_piece, then returns both.
def choose_piece():
    player_info = {}
    name = input("Player 1, what's your name? ")
    log("Player 1's name is: " + name)
    symbol = input("Player 1, choose a play piece (X/O): ")
    log("Player 1 chose " + symbol)
    while symbol not in ["X", "O", "x", "o"]:
        symbol = input("You chose " + symbol + ". This is not a game piece. Make sure to use either an 'X' or an 'O' as your piece: " )
    player_info["Player1"] = [name, symbol.upper()]
    log(player_info)
    name = input("Player 2, what's your name? ")
    log("Player 2's name is: " + name)
    if symbol.upper() == "X":
        symbol = "O"
        log(player_info["Player1"][0] + " is " + player_info["Player1"][1] + ". " + name + " is " + symbol)
    else:
        symbol = "X"
        log(player_info["Player1"][0] + " is " + player_info["Player1"][1] + ". " + name + " is " + symbol)
    player_info["Player2"] = [name, symbol]
    log(player_info)
    print(player_info["Player1"][0] + " is " + player_info["Player1"][1] + ". " + player_info["Player2"][0] + " is " + player_info["Player2"][1] + ". Now we are ready to play!\n")
    return player_info
    
def whos_turn(players, turn_count):
    if turn_count % 2 == 1:
        log("Play is odd. Go: " + players["Player1"][0] + players["Player1"][1])
        return players["Player1"][0], players["Player1"][1]
    else:
        log("Play is even. Go: " + players["Player2"][0] + players["Player2"][1])
        return players["Player2"][0], players["Player2"][1]

#Function checks which columns have space, asks player for input, checks input is viable
#Places the correct symbol in the chosen place and returns the amended board.
def play_turn(board, player, symbol):
    playable_columns = check_playable_columns(board)
    log("Columns in play are: " + str(playable_columns))
    col_choice = input("It is " + player + "'s turn. Choose a column from " + str(playable_columns) + ": ")
    log("Player chose: " + col_choice)
    col_choice = move_is_valid(playable_columns, col_choice)
    log("After checking, col_choice is: " + str(col_choice))
    amended_board, position = place_piece(board, symbol, col_choice)
    return amended_board, position

#Function checks which columns have space and passes back a list
def check_playable_columns(board):
    column_has_space = []
    for col in range(0, len(board)):
        if board[col][0] == " ":
            column_has_space.append((col + 1))
    log(column_has_space)
    return column_has_space   

#Takes the list of playable_columns and the choice of column and checks that the latter is an integer in the list, then returns it if valid.
def move_is_valid(list_of_columns, choice):
    try:
        num = int(choice)
    except ValueError:
        choice = input("That is not a column in " + str(list_of_columns) + ". Please choose again: ")
        col_choice = move_is_valid(list_of_columns, choice)
        return col_choice
    else:
        if num in list_of_columns:
            return num
        else:
            choice = input("That is not a column in " + str(list_of_columns) + ". Please choose again: ")
            col_choice = move_is_valid(list_of_columns, choice)
            return col_choice

#Function finds the lowest row in that column without a piece in and places the piece
def place_piece(board, symbol, col_choice):
    log(symbol)
    log(col_choice)
    row_index = -1
    col_index = col_choice - 1
    while row_index >= -len(board[0]):
        if board[col_index][row_index] != " ":
            row_index -= 1
            log(row_index)
        else:
            board[col_index][row_index] = symbol
            print("Placed an " + symbol + " in column " + str(col_choice) + "\n")
            log(board[col_index][row_index])
            row_index += len(board[0])
            log_symbol_and_position = (symbol, col_index, row_index)
            return board, log_symbol_and_position

def scan(position, direction):
    while True:
        position = (position[0] + direction[0], position[1] + direction[1])
        yield position

def run_length_in_direction(board, position, symbol, direction):
    run_length = 0
    for position_check in scan(position, direction):
        if position_check[0] in range(0, len(board)) and position_check[1] in range(0, len(board[0])):
            contents = board[position_check[0]][position_check[1]]
            log(contents)
            if contents == symbol:
                run_length += 1
            else:
                log(run_length)
                return run_length
        else:
            return run_length

def check_win(board, last_position_placed):
    position = (last_position_placed[1], last_position_placed[2])
    symbol = last_position_placed[0]
    log(position)
    log(symbol)
    log(run_length_in_direction(board, position, symbol, UP))
    log(run_length_in_direction(board, position, symbol, DOWN))
    log(run_length_in_direction(board, position, symbol, LEFT))
    log(run_length_in_direction(board, position, symbol, RIGHT))
    log(run_length_in_direction(board, position, symbol, UP_LEFT))
    log(run_length_in_direction(board, position, symbol, DOWN_RIGHT))
    log(run_length_in_direction(board, position, symbol, UP_RIGHT))
    log(run_length_in_direction(board, position, symbol, DOWN_LEFT))
    return (
        run_length_in_direction(board, position, symbol, UP) + run_length_in_direction(board, position, symbol, DOWN) + 1 >= 4 or
        run_length_in_direction(board, position, symbol, LEFT) + run_length_in_direction(board, position, symbol, RIGHT) + 1 >= 4 or
        run_length_in_direction(board, position, symbol, UP_LEFT) + run_length_in_direction(board, position, symbol, DOWN_RIGHT) + 1 >= 4 or
        run_length_in_direction(board, position, symbol, UP_RIGHT) + run_length_in_direction(board, position, symbol, DOWN_LEFT) + 1 >= 4
    )

def play_game():
    print("Welcome to my Connect 4 game!")
    board = create_board(int(choose_row()), int(choose_col()))
    player_info = choose_piece()
    print_board(board)
    turn_count = 1
    log("Turn count is: " + str(turn_count))
    while turn_count <= (len(board) * len(board[0])):
        player, symbol = whos_turn(player_info, turn_count)
        log(player)
        log(symbol)
        board, last_position_placed = play_turn(board, player, symbol)
        print_board(board)
        turn_count += 1
        log("Turn count is: " + str(turn_count))
        if check_win(board, last_position_placed):
            print("Congratulations! " + player + " has won!")
            return
    print("The board is full and no-one achieved 4 in a row. The game is tied.")
    

play_game()
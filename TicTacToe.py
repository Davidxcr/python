#Tic Tac Toe Game in Python.

#Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

#If game is still going

game_still_going = True

#Who won? or Tie?
winner = None

#who's turn is it?
current_player = "X"

#display the board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
  print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
  print(board[6] + " | " + board[7] + " | " + board[8] + " | ")


def play_game():

  #Display the initial board
  display_board()
  
  while game_still_going:
    #handle turn of a player
    handle_turn(current_player)

    check_if_game_over()

    # Flip to the other player.
    flip_player()

  #The game has ended
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


#Handle single player turn
def handle_turn(player):

  print(player + "'s turn")
  position = input("Choose a position from 1-9: ")

  while position not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):

    position = input("Invalid input. Choose a position from 1-9:  ")

  position = int(position) - 1

  if board[position] != "-":
    print("You can't go there. Go again.")

  board[position] = player
  display_board()

#check if the game is over  
def check_if_game_over():
  check_for_winner()
  check_if_tie()


#check if there is a winner
def check_for_winner():
  
  #set up global Variables
  global winner
  #check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #check diagonal
  diagonal_winner = check_diagonal()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return

#check rows for win
def check_rows():
  #Set up global Variables
  global game_still_going
  #check rows to see if they have the same values
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False
    #return winner X or O
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

#check columns for win
def check_columns():
  #Set up global Variables
  global game_still_going
  #check columns to see if they have the same values
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3:
    game_still_going = False
    #return winner X or O
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

#check if a win exists diagonally
def check_diagonal():
  #Set up global Variables
  global game_still_going
  #check rows to see if they have the same values
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[7] != "-"

  if diagonal_1 or diagonal_2:
    game_still_going = False
    #return winner X or O
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return

#check for a tie
def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False

  return


#Change player
def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return

play_game()
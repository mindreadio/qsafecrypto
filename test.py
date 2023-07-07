# A tictactoe game.
# 3 by 3 grid. 
# Goal of the game: 
# Draw is possible
 
# You need to show them the result as well;

# First player: |
# Second player : - 

#
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def board_view():
  for row in board:
    print('|'.join(row))
    print('-' * 5)
    
def check_win(player):
  # ROW CHECK
  for row in board:
    if all(cell == player for cell in row):
      return True
  
  # Column Check
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
    
  # 1st Diagonals Check
  if board[0][0] == board[1][1] == board[2][2] == player: 
    return True
  
  # 2nd Diagonals Check 
  if board[0][2] == board[1][1] == board[2][0] == player: 
    return True
  
    
def check_draw(player):
  for row in board:
    if ' ' in row:
      return False
  return True
    
def playing_the_game():
  current_player = "ROCKY"
  
  while True:
    board_view()
    
    # Tell players to mark a move
    print("Player", current_player, "turn")
    row = int(input('Please, mark down row (0-2): '))
    col = int(input('Please, mark down column (0-2): '))
    
    # Move from the current player
    board[row][col] = current_player
    
    if check_win(current_player):
      board_view()
      print("Winner is: ", current_player)
      break 

    if check_draw(current_player):
      board_view()
      print("Drawww!")
      break 
  
    current_player = "JESPER" if current_player == "ROCKY" else "ROCKY"
  
playing_the_game()
    

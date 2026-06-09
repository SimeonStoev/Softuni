class InvalidColumnException(Exception):
   pass




number_of_players = int(input("How many players? "))


players = [f"Player {n + 1}" for n in range(number_of_players)]


board = [[0 for _ in range(7)] for _ in range(6)]




def print_board():
   global board
   for i in range(6):
       print("[ ", end="")
       print(", ".join(map(str, board[i])), end="")
       print(" ]")




def is_board_fully_occupied():
   global board
   for i in range(6):
       for j in range(7):
           if board[i][j] == 0:
               return False
   return True




def reset_logic():
   global board
   board = [[0 for _ in range(7)] for _ in range(6)]




def play(column, player_count):
   global board
   if board[0][column] != 0:
       print(f"Column {column} already occupied. You miss your turn!")
       return


   for row in range(5, -1, -1):
       if board[row][column] == 0:
           board[row][column] = player_count
           return row


   return




def check_win(row, column):
   global board
   player_count = board[row][column]


   # horyzontal check
   curr_col = column
   numb_of_cells = 0
   while curr_col >= 0 and board[row][curr_col] == player_count:
       curr_col -= 1
       numb_of_cells += 1
   curr_col = column + 1
   while curr_col < 7 and board[row][curr_col] == player_count:
       curr_col += 1
       numb_of_cells += 1
   if numb_of_cells >= 4:
       return True


   # vertical check
   numb_of_cells = 0
   curr_row = row
   while curr_row >= 0 and board[curr_row][column] == player_count:
       curr_row -= 1
       numb_of_cells += 1
   curr_row = row + 1
   while curr_row < 6 and board[curr_row][column] == player_count:
       curr_row += 1
       numb_of_cells += 1
   if numb_of_cells >= 4:
       return True


   # left diagonal 1 check
   numb_of_cells = 0
   curr_row = row
   curr_col = column
   while curr_row >= 0 and curr_col >= 0 and board[curr_row][curr_col] == player_count:
       curr_row -= 1
       curr_col -= 1
       numb_of_cells += 1
   curr_row = row + 1
   curr_col = column + 1
   while curr_row < 6 and curr_col < 7 and board[curr_row][curr_col] == player_count:
       curr_row += 1
       curr_col += 1
       numb_of_cells += 1
   if numb_of_cells >= 4:
       return True


   # right diagonal 2 check
   numb_of_cells = 0
   curr_row = row
   curr_col = column
   while curr_row >= 0 and curr_col < 7 and board[curr_row][curr_col] == player_count:
       curr_row -= 1
       curr_col += 1
       numb_of_cells += 1
   curr_row = row + 1
   curr_col = column - 1
   while curr_row < 6 and curr_col >= 0 and board[curr_row][curr_col] == player_count:
       curr_row += 1
       curr_col -= 1
       numb_of_cells += 1
   if numb_of_cells >= 4:
       return True


   return False




print_board()


while True:
   for player in players:
       try:
           column = input(f"{player}, please choose a column\n")
           if column == "reset":
               reset_logic()
           else:
               column = int(column)
       except ValueError:
           print(f"Column must be of type int")
           raise
       if column <= 0 or column > 7:
           raise InvalidColumnException("Column must be between 1 and 7")
       row = play(column - 1, player[-1])
       print_board()
       if check_win(row, column - 1):
           print(f"The winner is player {player[-1]}")
           exit(0)


       if is_board_fully_occupied():
           print("The board is full! There is no winner")
           break
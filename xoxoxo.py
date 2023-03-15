board = [[' ' for _ in range(3)] for _ in range(3)]

def draw_board():
  print('-' * 9)
  for row in board:
    print('|', *row, '|')
  print('-' * 9)

def make_move(player, x, y):
  if board[x][y] != ' ':
    return False
  board[x][y] = player
  return True

def has_won(player):
  # check rows
  for row in board:
    if all(cell == player for cell in row):
      return True
  # check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
  # check diagonals
  if all(board[i][i] == player for i in range(3)):
    return True
  if all(board[i][2 - i] == player for i in range(3)):
    return True
  return False

def main():
  current_player = 'X'
  while True:
    draw_board()
    print(f'Player {current_player} turn')
    x, y = map(int, input('Enter coordinates: ').split())
    if not make_move(current_player, x - 1, y - 1):
      print('This cell is already occupied')
      continue
    if has_won(current_player):
      print(f'Player {current_player} has won')
      break
    current_player = 'O' if current_player == 'X' else 'X'
  draw_board()

main()

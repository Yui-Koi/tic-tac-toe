# Minimax algorithm with alpha beta pruning
def minimax(X, O, maximize, alpha, beta, cache):
  # Check transposition table
  state = (X, O, maximize)
  if state in cache:
    return cache[state]
 # Check wins
  if check_win(X):
    return 1 if not maximize else -1
  if check_win(O):
    return -1 if maximize else 1
  # Check draw
  if X | O == 0b111111111:
    return 0

  # Available moves to play
  moves = [i for i in range(9) if not (X | O) & masks[i]]
  
  if maximize: # Maximizing player's turn
    best_score = max(
      map(lambda i: minimax(X | masks[i], O, False, alpha, beta,
      cache), moves), default = -float('inf'))
    alpha = max(alpha, best_score)
    if beta <= alpha:
      return best_score
  else: # Minimizing player's turn
    best_score = min(
      map(lambda i: minimax(X, O | masks[i], True, alpha, beta,
      cache), moves), default = float('inf'))
    beta = min(beta, best_score)
    if beta <= alpha:
      return best_score

  cache[state] = best_score
  return best_score

# Get best move
def get_best_move(X, O, cache, symbol):
  moves = [i for i in range(9) if not (X | O) & masks[i]]
  if symbol == "X":
    return max(moves, key=lambda i: minimax(X | masks[i], O, False,
    -float('inf'), float('inf'), cache))
  else:
    return min(moves, key=lambda i: minimax(X, O | masks[i], True,
    -float('inf'), float('inf'), cache))

# Get user move
def user_move(X, O, symbol):
  while True:
    move = input(f"({symbol}) Input your move (1-9): ")
    if move.isdigit() and 1 <= int(move) <= 9:
      mask = masks[int(move)-1]
      if (X | O) & mask:
        print(f"That space is already taken!")
      else:
        return (X | mask, O) if symbol == "X" else (X, O | mask)
    else:
      print("Invalid input! Enter a number between 1 and 9.")

# Function to make a move for the current player
def make_move(X, O, turn, cache, players):
  if players[turn] == "You":
    X, O = user_move(X, O, turn)
  else:
    print("AI is thinking...") 
    move = get_best_move(X, O, cache, turn)
    if turn == "X":
      X |= masks[move]
    else:
      O |= masks[move]
  return X, O, cache

X, O = 0, 0
masks = [1 << i for i in range(9)][::-1]
win_mask = (0b111000000, 0b000111000, 0b000000111, 0b100100100, 0b010010010, 0b001001001, 0b100010001, 0b001010100)
print_board = lambda X, O: print("\n".join("|" + "|".join(" XO"[(X >> i) & 1 | ((O >> i) & 1) << 1] for i in range(8 - row * 3, 5 - row * 3, -1)) + "|" for row in range(3)))
check_win = lambda player_mask: any(player_mask & mask == mask for mask in win_mask)
cache = {}
  
# Game loop
def play_game(X, O, cache):
  print("Welcome to Tic Tac Toe!")
  player_symbol = input("Do you want to play as X or O? ").upper()
  ai_symbol = "O" if player_symbol == "X" else "X"
  print_board(X, O)
  turn = "X"
  players = {"X": "You" if player_symbol == "X" else "AI", "O": "You" if player_symbol == "O" else "AI"} # Map symbols to players
  while True:
    X, O, cache = make_move(X, O, turn, cache, players)
    print_board(X, O)
    if check_win(X if turn == "X" else O):
      print(f"Congratulations! {players[turn]} wins}!")
      break
    elif X | O == 0b111111111:
      print(f"It's a tie!")
      break
    turn = "O" if turn == "X" else "X"


play_game(X, O, cache)

from typing import Tuple

# Minimax algorithm with alpha beta pruning
def minimax(X: int, O: int, maximize: bool, alpha: float, beta: float, cache: dict) -> int:
  """
  Implement the Minimax algorithm with alpha-beta pruning to find the best move for the current player.
  Args:
    X (int): The current state of the board for the maximizing player (X).
    O (int): The current state of the board for the minimizing player (O).
    maximize (bool): True if the current player is the maximizing player, False otherwise.
    alpha (float): The current best score for the maximizing player.
    beta (float): The current best score for the minimizing player.
    cache (dict): A dictionary to store the results of previous evaluations (transposition table).
  Returns:
    int: The best score for the current player.
  """
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
  # All available moves
  moves = [i for i in range(9) if not (X | O) & masks[i]]
  if maximize: # Maximizing player's turn
    best_score = max(
        map(lambda i: minimax(X | masks[i], O, False, alpha, beta,
        cache), moves), default = -float('inf'))
    alpha = max(alpha, best_score)
    if beta <= alpha: return best_score
  else: # Minimizing player's turn
    best_score = min(
        map(lambda i: minimax(X, O | masks[i], True, alpha, beta,
        cache), moves), default = float('inf'))
    beta = min(beta, best_score)
    if beta <= alpha: return best_score
  cache[state] = best_score
  return best_score

# Get best move
def get_best_move(X: int, O: int, cache: dict, symbol: str) -> int:
  """
  Find the best move for the current player based on the Minimax algorithm.
  Args:
    X (int): The current state of the board for the maximizing player (X).
    O (int): The current state of the board for the minimizing player (O).
    cache (dict): A dictionary to store the results of previous evaluations (transposition table).
    symbol (str): The symbol of the current player ('X' or 'O').
  Returns:
    int: The index of the best move for the current player.
  """
  moves = [i for i in range(9) if not (X | O) & masks[i]]
  maximize = symbol == "X"
  return max(moves, key=lambda i: minimax(X | masks[i], O, not maximize, -float('inf'), float('inf'), cache)) \
  if maximize else min(moves, key=lambda i: minimax(X, O | masks[i], not maximize, -float('inf'), float('inf'), cache))

# Get user move
def user_move(X: int, O: int, symbol: str) -> int:
  """
  Get the user's move and update the board accordingly.
  Args:
    X (int): The current state of the board for the maximizing player (X).
    O (int): The current state of the board for the minimizing player (O).
    symbol (str): The symbol of the current player ('X' or 'O').
  Returns:
    int: The updated states of the board for the player (X) or player (O).
  """
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
def make_move(X: int, O: int, turn: str, players: dict, cache: dict) -> Tuple[int, int]:
  """
  Make a move for the current player, either by the user or the AI.
  Args:
    X (int): The current state of the board for the maximizing player (X).
    O (int): The current state of the board for the minimizing player (O).
    turn (str): The symbol of the current player ('X' or 'O').
    cache (dict): A dictionary to store the results of previous evaluations (transposition table).
    players (dict): A dictionary mapping player symbols to their names ('You' or 'AI').
  Returns:
    Tuple[int, int]: The updated states of the board for the maximizing player (X) and the minimizing player (O).
  """
  if players[turn] == "Player":
    X, O = user_move(X, O, turn)
  else:
    print("AI is thinking...") 
    move = get_best_move(X, O, cache, turn)
    if turn == "X":
      X |= masks[move]
    else:
      O |= masks[move]
  return X, O

def initialise_game() -> Tuple[str, str]:
  """
  This function prompts the user to choose their player symbol (X or O) and determines the AI's symbol.
  Returns:
    Tuple[str, str]: The player's symbol and the AI's symbol.
  """
  print("Welcome to Tic Tac Toe!")
  player_symbol = input("Do you want to play as X or O? ").upper()
  if player_symbol not in ["X", "O"]:
    return initialise_game()
  ai_symbol = switch_symbol("X", "O", player_symbol, "O")
  return player_symbol, ai_symbol

# Game loop
def play_game(X, O) -> None:
  """
  This function handles the main game loop, including making moves, checking for wins, and determining the winner.
  Args:
    X (int): The current state of the board for the maximizing player (X).
    O (int): The current state of the board for the minimizing player (O).
  Returns:
    None
  """
  player_symbol, ai_symbol = initialise_game()
  turn, cache = "X", {}
  print_board(X, O)
  players = {"X": switch_symbol("Player", "AI", player_symbol, "X"), "O": switch_symbol("Player", "AI", player_symbol, "O")}
  while True:
    X, O = make_move(X, O, turn, players, cache)
    print_board(X, O)
    if check_win(switch_symbol(X, O, turn, "X")):
      print(f"Congratulations! {players[turn]} wins!")
      break
    elif X | O == 0b111111111:
      print(f"It's a tie!")
      break
    turn = switch_symbol("X", "O", turn, "O")

X, O = 0, 0
masks = [1 << i for i in range(9)][::-1]
win_mask = (0b111000000, 0b000111000, 0b000000111, 0b100100100, 0b010010010, 0b001001001, 0b100010001, 0b001010100)
print_board = lambda X, O: print("\n".join("|" + "|".join(" XO"[(X >> i) & 1 | ((O >> i) & 1) << 1] for i in range(8 - row * 3, 5 - row * 3, -1)) + "|" for row in range(3)))
check_win = lambda player_mask: any(player_mask & mask == mask for mask in win_mask)
switch_symbol = lambda X, O, symbol, shift: X if symbol == shift else O

play_game()

# **Tic-Tac-Toe with Minimax alpha beta pruning and bitboards**

A hobby project implementing the Minimax algorithm with alpha-beta pruning to play Tic Tac Toe. This implementation uses bitboards to efficiently represent the game state and uses a transposition table to reduce computational complexity.

# **Features**
* **Minimax Algorithm**: Implemented with alpha-beta pruning to find the best move for the current player.
* **Bitboard Representation**: Efficiently represents the game state using bitboards, allowing for fast evaluation of moves.
* **Transposition Table**: Stores the results of previous evaluations to reduce computational complexity.
* **User-Friendly Interface**: Play against the AI or make moves manually.
* **Game Loop**: Handles the main game loop, including making moves, checking for wins, and determining the winner.

# **How to Play**

1. Clone the repository and run the script.
2. Choose your player symbol (X or O) when prompted.
3. Make moves by entering the number of the space where you'd like to place your symbol (1-9).
4. The AI will make its moves automatically.
5. The game will end when a player wins or the board is full (tie).

# **Technical Details**

* **Bitboard Masks**: Used to efficiently update the game state and check for wins.
* **Minimax Function**: Implements the Minimax algorithm with alpha-beta pruning to find the best move.
* **Get Best Move**: Finds the best move for the current player based on the Minimax algorithm.
* **User Move**: Handles user input and updates the game state accordingly.

# **Contributing**

If you'd like to contribute to this project, please open a pull request with your suggested changes.

# Tic-Tac-Toe Bitboard Implementation with Minimax Alpha-Beta Pruning

This is a Python implementation of the Tic Tac Toe game, with an AI player that uses the Minimax algorithm with Alpha-Beta pruning to determine the best move.

## Features

- Minimax algorithm with Alpha-Beta pruning for the AI player
- Transposition table for caching previous evaluations
- Terminal interface for playing against the AI
- Supports both X and O as player symbols

## Usage

1. Run the script to start the game.
2. When prompted, choose whether you want to play as X or O.
3. Input your moves by entering a number between 1 and 9 (1 for the top-left corner, 9 for the bottom-right corner).
4. The AI will make its move, and the game will continue until a winner is determined or the game ends in a tie.

## How it Works

The main components of the implementation are:

1. `minimax()` function: This function implements the Minimax algorithm with Alpha-Beta pruning to determine the best move for the current player.
2. `get_best_move()` function: This function uses the `minimax()` function to find the best move for the current player.
3. `user_move()` function: This function handles the user's input and updates the board accordingly.
4. `make_move()` function: This function determines whether the current move should be made by the user or the AI and updates the board accordingly.
5. `play_game()` function: This function manages the main game loop, including initializing the game, making moves, checking for wins, and determining the winner.

The game uses a bit-board representation to efficiently store the current state of the board, and the `masks` list is used to represent the possible moves on the board.

## Dependencies

This implementation does not require any external dependencies. It uses only standard Python libraries.

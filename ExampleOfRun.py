import chess

# Create a new board
board = chess.Board()

# Make a move as the human player
human_move = chess.Move.from_uci("e2e4")
board.push(human_move)

# Get the AI's best move
ai_move = best_move(board, depth=3)

# Print the AI's move in UCI format
print(ai_move.uci())

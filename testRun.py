board = chess.Board()

while not board.is_game_over():
    if board.turn == chess.WHITE:
        # Human player's turn
        move = input("Your move: ")
        move = chess.Move.from_uci(move)
        if move in board.legal_moves:
            board.push(move)
        else:
            print("Invalid move")
    else:
        # AI player's turn
        move = best_move(board, depth=3)
        board.push(move)
        print("AI's move:", move.uci())

print("Game over")

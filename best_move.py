def best_move(board, depth):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for move in board.legal_moves:
        board.push(move)
        eval = minimax_alpha_beta(board, depth-1, alpha, beta, False)
        board.pop()
        if eval > best_eval:
            best_eval = eval
            best_move = move
        alpha = max(alpha, eval)
    return best_move
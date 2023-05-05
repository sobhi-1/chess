def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board)
    
    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth-1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth-1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval